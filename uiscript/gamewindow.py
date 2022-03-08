import gameInfo

		{ 
			"name":"BiyologButton", 
			"type":"button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : str(gameInfo.CONFIG_YOL)+"biyolog/biyologbutton.tga",
			"over_image" : str(gameInfo.CONFIG_YOL)+"biyolog/biyologbutton_2.tga",
			"down_image" : str(gameInfo.CONFIG_YOL)+"biyolog/biyologbutton_3.tga",

			"children" : 
			(
				{ 
					"name":"BiyologButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":"Biolog", 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
	