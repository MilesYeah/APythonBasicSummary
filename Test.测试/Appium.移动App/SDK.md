

1.Android SDK
	环境：
		Android：基于java开发的一个针对移动端APP的开发平台
		java：jdk1.8，http://jdk.android-studio.org
		Android SDK：
			http://tools.android-studio.org/index.php/sdk
			
			SDK Manager.exe安装
			
		环境变量的配置：
			1.配置ANDROID_HOME，值是SDK的路径
			2.%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools;

		检查SDK环境：
			adb version
			Android Debug Bridge version 1.0.41
			
			注意：各种形式的手机助手，请卸载掉

	SDK根本用途是什么？
		操作手机

	1.你得有一台手机	
		真机
		模拟器：夜神，mumu
		
	2.连接电脑和手机
		WiFi：需要root手机的
		USB数据线连接：
			1.在手机上面开启USB调试模式
			2.使用SDK里面的adb连接电脑和手机
				真机：adb devices，会自动连接
				模拟器：adb connect 127.0.0.1:7555/62001
	3.操作手机
		adb命令
			adb shell input tap x y
