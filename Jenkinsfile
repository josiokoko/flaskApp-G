pipeline {
	
    agent any 
	
    environment {
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    }

    tools {
      terraform "terraform21109"
    }
	
    stages {

        stage('Checkout') {
          agent any
          steps {
              checkout scm
          }
        }
        
        stage('Docker Build') {
          agent any
          steps {
              sh 'docker build -t josiokoko/flaskapp:0.${BUILD_NUMBER} .'
          }
        }
        

        stage('Docker Push') {
          agent any
          environment {
              DOCKER_HUB_CREDS = credentials('joseph-dockerhub-creds')
          }
          steps {
	        sh "docker tag josiokoko/flaskapp:0.${BUILD_NUMBER} josiokoko/flaskapp:0.${BUILD_NUMBER}"
            // sh 'docker login -u $DOCKER_HUB_CREDS_USR -p $DOCKER_HUB_CREDS_PSW'
	        sh 'echo $DOCKER_HUB_CREDS_PSW | docker login -u $DOCKER_HUB_CREDS_USR --password-stdin'
            sh 'docker push josiokoko/flaskapp:0.${BUILD_NUMBER}'
          }
        }

        stage ('Another Build and Push') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'joseph-dockerhub-creds') {
                        def dockerImage = docker.build('josiokoko/another-flask:0.${BUILD_ID}')
                        dockerImage.push()
                    }
                }
            }
        }

        
        stage ('Infrastructure Provisioning'){
            parallel {
                stage('Terraform Init'){
                    steps {
                        sh label: '', script: 'terraform init'
                    }
                } 
                
                stage('Terraform Plan'){
                    steps {
                        sh label: '', script: 'terraform plan'
                    }
                } 
            }
        }


    }
}
