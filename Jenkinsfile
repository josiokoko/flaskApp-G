pipeline {
	
    agent none 
	
    stages {
        
        stage('Docker Build') {
          agent any
          steps {
              sh 'docker build -t josiokoko/flaskapp:${env.BUILD_ID} .'
          }
        }
        
        stage('Docker Push') {
          agent any
          environment {
              DOCKER_HUB_CREDS = credentials('joseph-dockerhub-creds')
          }
          steps {
	      sh "docker -t josiokoko/flaskapp:${env.BUILD_ID} josiokoko/flaskapp"
              sh "docker login -u $DOCKER_HUB_CREDS_USR -p $DOCKER_HUB_CREDS_PSW"
	      // sh 'echo $DOCKER_HUB_CREDS_PSW | docker login -u $DOCKER_HUB_CREDS_USR --password-stdin'
              sh 'docker push josiokoko/flaskapp'
          }
        } 
        
    }
}
