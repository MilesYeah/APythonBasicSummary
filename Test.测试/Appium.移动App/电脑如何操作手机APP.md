1.电脑如何操作手机APP
	1.手机
		模拟器：
			mumu，夜神，逍遥
		
		真机：
			华为，小米，vivo
			
	2.连接电脑和手机
		Android SDK：
			Android：Google开源的基于java的移动APP开发平台
			JDK：http://jdk.android-studio.org/
			SDK：http://tools.android-studio.org/index.php/sdk
				Android SDK tools
				Android SDK platform-tools
				Google USB Driver

				环境变量配置：
					ANDROID_HOME = E:\software\Android\sdk
					%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools;

				检测：
					adb version

		连接：
			USB调试模式
				开启usb调试模式
			
			WIFI连接
				需要root手机

			adb连接：
				手机：
					adb devices
				
				模拟器：
					adb connect 127.0.0.1:7555
					adb devices
