pipeline {
    agent any
    environment {
        IMAGE_NAME = "susantaadak/django-app"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/Susanta-Adak/CI_CD_Practice.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials-id', url: 'https://hub.docker.com/u/susantaadak']) {
                        sh 'docker push $IMAGE_NAME'
                    }
                }
            }
        }
        stage('Deploy on Master Node') {
            steps {
                script {
                    sh '''
                    docker container stop django_app || true
                    docker container rm django_app || true
                    docker run -d --name django_app -p 8000:8000 $IMAGE_NAME
                    '''
                }
            }
        }
    }
}
