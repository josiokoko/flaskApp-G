pipeline {
    agent any
    
    stages {
    
    
        stage('Checkout'){
            steps{
                sh "echo this is checkout stage"
            }
        }
        
        
        stage('BuildStage') {
            steps{
                sh "echo build docker image"
                sh "echo push docker to dockerHub"
            }
        }
        
        
        stage('Provision') {
            steps {
                sh "echo provision infrastructure"
            }
        }
        
        
        stage('Deploy') {
            steps{
                sh "echo provision infrastructure"
            }
         }
         
    }
}
