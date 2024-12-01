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
        stage('Deploy on Master Node') {
            steps {
                script {
                    sh 'docker compose down && docker compose up -d --build'
                }
            }
        }
    }
}
