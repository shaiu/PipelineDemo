#!/usr/bin/env groovy
pipeline {
    agent {
        docker { image 'python:2.7' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
				cat app/main.py
            }
        }
    }
}
