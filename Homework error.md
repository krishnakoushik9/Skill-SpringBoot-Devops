![[Pasted image 20250707220256.png]]
```
Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-07-07T22:02:12.037+05:30 ERROR 9428 --- [demo2] [           main] o.s.b.d.LoggingFailureAnalysisReporter   : 

***************************
APPLICATION FAILED TO START
***************************

Description:

Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.

Reason: Failed to determine suitable jdbc url


Action:

Consider the following:
	If you want an embedded database (H2, HSQL or Derby), please put it on the classpath.
	If you have database settings to be loaded from a particular profile you may need to activate it (no profiles are currently active).


Process finished with exit code 1
```
==It finally worked==
![[Pasted image 20250707221200.png]]
