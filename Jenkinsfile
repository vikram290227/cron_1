pipeline {
    agent any

    environment {
        ACR_LOGIN_SERVER = 'linuxcontainerregistry01.azurecr.io'
        ACR_USERNAME = 'linuxcontainerregistry01'
        ACR_PASSWORD =  BHPtrpaFy+ZhAtKwXvPx1kmHK2Gr4SvfQ8vxKHu2HF+ACRBAfZSK
        DOCKER_IMAGE = "${ACR_LOGIN_SERVER}/cronjob"  // Docker image name
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
                    def version = "v${env.BUILD_NUMBER}" // Use Jenkins build number for version
                    sh """
                    docker build -t ${DOCKER_IMAGE}:${version} .
                    """
                }
            }
        }

        stage('Push Docker Image to ACR') {
            steps {
                script {
                    def version = "v${env.BUILD_NUMBER}"
                    sh """
                    echo ${ACR_PASSWORD} | docker login ${ACR_LOGIN_SERVER} --username ${ACR_USERNAME} --password-stdin
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
