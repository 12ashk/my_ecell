Stepper ODEStepper(DE){
}

System System(/)
{
	StepperID DE;
	Variable Variable(SIZE){
		Value 1.0;
	}
	Variable Variable(cyclin){
		Value 0.01;
	}
	Variable Variable(cdc2){
		Value 0.01;
	}
	Variable Variable(cp){
		Value 0.01;
	}
	Process ExpressionFluxProcess(dcdt){
		vi 0.023;
		vd 0.1;
		Kd 0.02;
		kd 0.00333;
		Expression "vi - vd*X.Value*C.Value/(Kd+C.Value) - kd*C.Value";
		VariableReferenceList [C :.:cyclin +1][X :.:cp 0];
	}
	Process ExpressionFluxProcess(dMdt){
		Kc 0.3;
		Vm_one 0.5;
		K_one 0.1;
		V_two 0.167;
		K_two 0.1;
		Expression "C.Value*Vm_one*(1-M.Value)/((Kc+C.Value)*(K_one+(1-M.Value))) - V_two*M.Value/(K_two+M.Value)";
		VariableReferenceList [M :.:cdc2 +1][C :.:cyclin 0];
	}
	Process ExpressionFluxProcess(dXdt){
		Vm_three 0.2;
		K_three 0.1;
		V_four 0.1;
		K_four 0.1;
		Expression "M.Value*Vm_three*(1-X.Value)/(K_three+(1-X.Value)) - V_four*X.Value/(K_four+X.Value)";
		VariableReferenceList [X :.:cp +1][M :.:cdc2 0];
	}
}
