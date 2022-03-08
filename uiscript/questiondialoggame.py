import uiScriptLocale

WIDTH = 400-46
HEIGHT = 105

window = {
	"name" : "QuestionDialogGame",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : WIDTH,
			"height" : HEIGHT,

			"children" :
			(
				{
					"name" : "message",
					"type" : "text",

					"x" : 0,
					"y" : 38,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.MESSAGE,

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "kapat",
					"type" : "button",

					"x" : WIDTH-23,
					"y" : 8,

					"width" : 61,
					"height" : 21,

					#"horizontal_align" : "center",

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : -90,
					"y" : 63,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.YES,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "orta",
					"type" : "button",

					"x" : 0,
					"y" : 63,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.NO,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "cancel",
					"type" : "button",

					"x" : 40+49,
					"y" : 63,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.NO,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}