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
                    // Login to Azure using Service Principal
                    withCredentials([string(credentialsId: 'acr-client-secret', variable: 'ACR_CLIENT_SECRET')]) {
                        bat """
                        call az login --service-principal --username %ACR_CLIENT_ID% --password %ACR_CLIENT_SECRET% --tenant %ACR_TENANT_ID%
                        call az acr login --name ${env.ACR_LOGIN_SERVER.split('\\.')[0]}
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
