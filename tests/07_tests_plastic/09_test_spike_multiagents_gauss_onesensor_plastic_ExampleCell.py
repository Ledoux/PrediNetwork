#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#set
BrianingDebugVariable=25.

#set
AgentUnitsInt=1000

#Define
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'BrianingStepTimeFloat':0.01,
			'-Populations':[
				('|Sensor',{
					'RecordingLabelVariable':[0,1],
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Encod':{
							'BrianingDebugVariable':BrianingDebugVariable
						}
					}
				}),
				('|Agent',{
					'RecordingLabelVariable':[0,1],
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Fast':{
							'BrianingDebugVariable':BrianingDebugVariable,
							'RecordingLabelVariable':[0,1,2]
						}
					},
					#'LeakingNoiseStdVariable':0.01
				}),
				('|Decoder',{
					'RecordingLabelVariable':[0,1],
					#'BrianingDebugVariable':BrianingDebugVariable
					'-Interactions':{
						'|Slow':{
							#'BrianingDebugVariable':BrianingDebugVariable,
							#'LeakingWeigthVariable':0.
						}
					}
				})
			]
		}
	).predict(
		_AgentUnitsInt=AgentUnitsInt,
		_CommandVariable="#custom:#clock:50*ms:2.5*(1.*mV+1.*mV*(int(t==50*ms)+int(t==150*ms)))",#2.,
		_DecoderVariable="#array",
		_DecoderStdFloat = SYS.numpy.sqrt(AgentUnitsInt) * 0.4, #need to make an individual PSP around 1 mV
		_DecoderMeanFloat = AgentUnitsInt * 0.5, 
		_AgentResetVariable = -70., #big cost to reset neurons and make the noise then decide who is going to spike next
		_AgentNoiseVariable = 1., #noise to make neurons not spiking at the same timestep
		_AgentThresholdVariable = -57.,
		_AgentRefractoryVariable=0.5,
		_FastPlasticBool=True,
		_FastLearnRateFloat=0.1,
		_InteractionStr = "Spike"
	).simulate(
		500.
	)

#/###################/#
# View
#

MyPredicter.mapSet(
		{
			'PyplotingFigureVariable':{
				'figsize':(10,8)
			},
			'PyplotingGridVariable':(30,30),
			'-Panels':[
				(
					'|Run',
					[
						(
							'-Charts',
							[
								(
									'|Sensor_I_Command',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':2
										}
									}
								),
								(
									'|Sensor_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':2
										}
									}
								),
								(
									'|Agent_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':1
										}
									}
								),
								(
									'|Agent_Default_Events',{}
								),
								(
									'|Decoder_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':1
										}
									}
								)
							]
						)
					]
				)
			]
		}
	).view(
	).pyplot(
	).show(
	)

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyPredicter is ')
SYS._print(MyPredicter) 

