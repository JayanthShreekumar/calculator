pipeline {
	agent {
		docker {
			image 'jayantha:1.0'
		}
	}
	stages {
		stage('Build') {
			steps {
				sh 'python src/calc/Calculator.py'
			}
		}
		stage('Test') {
			steps {
				sh 'pytest'
			}
		}
	}
}
