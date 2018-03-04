#!/usr/bin/env groovy
pipeline {
    agent {
        docker { image 'python:2.7' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'export PYTHONPATH=${PWD};cd test;python -m unittest test_main'
            }
        }
    }
}
