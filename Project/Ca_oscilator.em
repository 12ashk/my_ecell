Stepper ODEStepper(DE){
}

System System(/)
{
	StepperID DE;
	Variable Variable(SIZE){
		Value 1.0;
	}	
	Variable Variable(Z){
		Value 1.6;
	}
	Variable Variable(Y){
		Value 0.3;
	}
	Process ExpressionFluxProcess(v0){
		k 1.0;
		Expression "k";
		VariableReferenceList [Z1 :.:Z +1];
	}
	Process ExpressionFluxProcess(v1){
		k 7.3;
		beta 0.7;
		Expression "beta*k";
		VariableReferenceList [Z1 :.:Z +1];
	}
	Process ExpressionFluxProcess(v2){
		Vm2 65.0;
		K2 1.0;
		n 2;
		Expression "Vm2*pow(Z1.Value, n)/(pow(K2, n) + pow(Z1.Value, n))";
		VariableReferenceList [Z1 :.:Z -1][Y1 :.:Y +1];
	}
	Process ExpressionFluxProcess(v3){
		Vm3 500.0;
		Kr 2.0;
		Ka 0.9;
		m 2;
		p 4;
		Expression "Vm3*pow(Y1.Value, m) * pow(Z1.Value, p)/((pow(Kr, m) + pow(Y1.Value, m))*(pow(Ka, p) + pow(Z1.Value, p)))";
		VariableReferenceList [Z1 :.:Z +1][Y1 :.:Y -1];
	}
	Process ExpressionFluxProcess(v4){
		kf 1.0;
		Expression "kf*Y1.Value";
		VariableReferenceList[Z1 :.:Z +1][Y1 :.:Y -1];
	}
	Process ExpressionFluxProcess(v5){
		k 10.0;
		Expression "k*Z1.Value";
		VariableReferenceList[Z1 :.:Z -1];
	}
}
