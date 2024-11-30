pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "linuxcontainerregistry01.azurecr.io"
        IMAGE_NAME = "cronjob"
        HELM_CHART_PATH = "./helm-chart"
        KUBECONFIG = credentials('kubeconfig') // Kubernetes config from Jenkins credentials
        ACR_CREDENTIALS = credentials('acr_credentials') // ACR credentials from Jenkins credentials
    }

    parameters {
        string(name: 'IMAGE_TAG', defaultValue: 'latest', description: 'Tag for the Docker image to deploy')
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/vikram290227/cron_1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: $DOCKER_REGISTRY/$IMAGE_NAME:${params.IMAGE_TAG}"
                    sh """
                    docker build -t $DOCKER_REGISTRY/$IMAGE_NAME:${params.IMAGE_TAG} .
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image to $DOCKER_REGISTRY"
                    sh """
                    docker login $DOCKER_REGISTRY -u ${ACR_CREDENTIALS_USR} -p ${ACR_CREDENTIALS_PSW}
                    docker push $DOCKER_REGISTRY/$IMAGE_NAME:${params.IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy with Helm') {
            steps {
                script {
                    echo "Deploying with Helm..."

                    // Define task configurations
                    def tasks = [
                        [name: "task1-release", valuesFile: "values-cronjob-task1.yaml"],
                        [name: "task2-release", valuesFile: "values-cronjob-task2.yaml"],
                        [name: "task3-release", valuesFile: "values-cronjob-task3.yaml"]
                    ]

                    // Deploy each task
                    tasks.each { task ->
                        echo "Deploying ${task.name} with values file: ${task.valuesFile}"
                        sh """
                        helm upgrade --install ${task.name} $HELM_CHART_PATH \
                            -f $HELM_CHART_PATH/${task.valuesFile} \
                            --set image.repository=$DOCKER_REGISTRY/$IMAGE_NAME \
                            --set image.tag=${params.IMAGE_TAG} \
                            --kubeconfig ${env.KUBECONFIG}
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully. All Helm releases deployed with image tag: ${params.IMAGE_TAG}"
        }
        failure {
            echo "Pipeline failed. Please review the logs to debug the issue."
        }
    }
}
