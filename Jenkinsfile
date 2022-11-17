pipeline {
	
    agent any 
	
    // environment {
    //     AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
    //     AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    // }
	
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
              // sh 'docker build -t josiokoko/flaskapp:${env.BUILD_ID} .'
              sh 'docker build -t josiokoko/flaskapp:001 .'
          }
        }
        
        stage('Docker Push') {
          agent any
          environment {
              DOCKER_HUB_CREDS = credentials('joseph-dockerhub-creds')
          }
          steps {
	      sh "docker tag josiokoko/flaskapp:001 josiokoko/flaskapp"
              sh "docker login -u $DOCKER_HUB_CREDS_USR -p $DOCKER_HUB_CREDS_PSW"
	      // sh 'echo $DOCKER_HUB_CREDS_PSW | docker login -u $DOCKER_HUB_CREDS_USR --password-stdin'
              sh 'docker push josiokoko/flaskapp'
          }
        } 
        
    }
}
