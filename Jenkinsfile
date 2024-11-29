pipeline {
    agent any

    environment {
        ACR_LOGIN_SERVER = 'linuxcontainerregistry01.azurecr.io'
        ACR_CLIENT_ID = '<service-principal-client-id>'      // Replace with actual Service Principal client ID
        ACR_TENANT_ID = '<tenant-id>'                        // Replace with actual Azure Tenant ID
        DOCKER_IMAGE = "${ACR_LOGIN_SERVER}/cronjob"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def version = "v${env.BUILD_NUMBER}"
                    bat """
                    docker build -t ${DOCKER_IMAGE}:${version} .
                    """
                }
            }
        }

        stage('Login to ACR') {
    steps {
        script {
            withCredentials([string(credentialsId: 'acr-client-secret', variable: 'ACR_CLIENT_SECRET')]) {
                bat """
                echo AZ CLI PATH: %PATH%
                echo Logging in to Azure CLI with Service Principal
                az login --service-principal --username "afb160bc-5751-4296-9539-770dc63149b0" --password "K9i8Q~UlwCjYqN3i4uSDvxAjQ2xtrqGy4hF76bIP" --tenant "25aa82fa-747f-4dd4-8b6d-a3014328e38b"
                az acr login --name linuxcontainerregistry01
                """
            }
        }
    }
}

        stage('Push Docker Image to ACR') {
            steps {
                script {
                    def version = "v${env.BUILD_NUMBER}"
                    bat """
                    docker login linuxcontainerregistry01.azurecr.io -u afb160bc-5751-4296-9539-770dc63149b0 -p "K9i8Q~UlwCjYqN3i4uSDvxAjQ2xtrqGy4hF76bIP"
                    docker push ${DOCKER_IMAGE}:${version}
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image has been successfully pushed to ACR!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
