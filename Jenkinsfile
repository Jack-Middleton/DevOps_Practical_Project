pipeline {
    agent any
    stages {
        // stage('test') {
        //     steps {
        //         dir('flask-app') {
        //             sh "rm application/tests/test_int*"
        //             sh "bash test_basic.sh"
        //         }
        //     }
        // }  uncomment when tests are written
        stage('build and push') {
            environment {
                DOCKER_CREDS = credentials('docker-creds')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
            }
        }
        stage('deploy stack') {
            steps {
                sh "scp ./docker-compose.yaml jenkins@ansible-sm:/home/jenkins/docker-compose.yaml"
                sh "scp ./nginx.conf jenkins@ansible-sm:/home/jenkins/nginx.conf"
                sh "ssh jenkins@ansible-sm < deploy.sh"
            }
        }
    }
    // post {
    //     always {
    //         archiveArtifacts artifacts: "*/htmlcov/*"
    //     }
    // } uncomment when testing written
}