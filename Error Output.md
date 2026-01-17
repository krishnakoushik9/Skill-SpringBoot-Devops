
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.5.3)

2025-06-30T10:08:15.918+05:30  INFO 169761 --- [demo] [           main] c.legion.learning.demo.DemoApplication   : Starting DemoAppli
cation using Java 17.0.15 with PID 169761 (/home/krsna/Desktop/Subbu uncle classes/demo/demo/target/classes started by krsna in /home/krsna/Desktop/Subbu uncle classes/demo)                                                                                             2025-06-30T10:08:15.921+05:30  INFO 169761 --- [demo] [           main] c.legion.learning.demo.DemoApplication   : No active profile 
set, falling back to 1 default profile: "default"                                                                                    2025-06-30T10:08:17.019+05:30  INFO 169761 --- [demo] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized
 with port 8080 (http)                                                                                                               2025-06-30T10:08:17.034+05:30  INFO 169761 --- [demo] [           main] o.apache.catalina.core.StandardService   : Starting service [
Tomcat]                                                                                                                              2025-06-30T10:08:17.035+05:30  INFO 169761 --- [demo] [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet e
ngine: [Apache Tomcat/10.1.42]                                                                                                       2025-06-30T10:08:17.100+05:30  INFO 169761 --- [demo] [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Sprin
g embedded WebApplicationContext                                                                                                     2025-06-30T10:08:17.102+05:30  INFO 169761 --- [demo] [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicatio
nContext: initialization completed in 1101 ms                                                                                        2025-06-30T10:08:17.355+05:30  WARN 169761 --- [demo] [           main] ConfigServletWebServerApplicationContext : Exception encounte
red during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'requestMappingHandlerMapping' defined in class path resource [org/springframework/boot/autoconfigure/web/servlet/WebMvcAutoConfiguration$EnableWebMvcConfiguration.class]: Ambiguous mapping. Cannot map 'maths' method                                com.legion.learning.demo.Maths#sum(int, int)
to {GET [/sum]}: There is already 'controller1' bean method
com.legion.learning.demo.Controller1#handleGet() mapped.
2025-06-30T10:08:17.362+05:30  INFO 169761 --- [demo] [           main] o.apache.catalina.core.StandardService   : Stopping service [
Tomcat]                                                                                                                              2025-06-30T10:08:17.388+05:30  INFO 169761 --- [demo] [           main] .s.b.a.l.ConditionEvaluationReportLogger : 

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-06-30T10:08:17.412+05:30 ERROR 169761 --- [demo] [           main] o.s.boot.SpringApplication               : Application run fa
iled                                                                                                                                 
org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'requestMappingHandlerMapping' defined in clas
s path resource [org/springframework/boot/autoconfigure/web/servlet/WebMvcAutoConfiguration$EnableWebMvcConfiguration.class]: Ambiguous mapping. Cannot map 'maths' method                                                                                                com.legion.learning.demo.Maths#sum(int, int)
to {GET [/sum]}: There is already 'controller1' bean method
com.legion.learning.demo.Controller1#handleGet() mapped.
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFac
tory.java:1826) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                              at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFacto
ry.java:607) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                 at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory
.java:529) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                   at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:339) ~[spring-be
ans-6.2.8.jar:6.2.8]                                                                                                                         at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:373)
 ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                             at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:337) ~[spring-beans-6.2.8
.jar:6.2.8]                                                                                                                                  at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:202) ~[spring-beans-6.2.8.j
ar:6.2.8]                                                                                                                                    at org.springframework.beans.factory.support.DefaultListableBeanFactory.instantiateSingleton(DefaultListableBeanFactory.java:
1222) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                        at org.springframework.beans.factory.support.DefaultListableBeanFactory.preInstantiateSingleton(DefaultListableBeanFactory.ja
va:1188) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                     at org.springframework.beans.factory.support.DefaultListableBeanFactory.preInstantiateSingletons(DefaultListableBeanFactory.j
ava:1123) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                                    at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.
java:987) ~[spring-context-6.2.8.jar:6.2.8]                                                                                                  at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:627) ~[spring-conte
xt-6.2.8.jar:6.2.8]                                                                                                                          at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext
.java:146) ~[spring-boot-3.5.3.jar:3.5.3]                                                                                                    at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:752) ~[spring-boot-3.5.3.jar:3.5.3]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:439) ~[spring-boot-3.5.3.jar:3.5.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:318) ~[spring-boot-3.5.3.jar:3.5.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1361) ~[spring-boot-3.5.3.jar:3.5.3]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1350) ~[spring-boot-3.5.3.jar:3.5.3]
        at com.legion.learning.demo.DemoApplication.main(DemoApplication.java:10) ~[classes/:na]
Caused by: java.lang.IllegalStateException: Ambiguous mapping. Cannot map 'maths' method 
com.legion.learning.demo.Maths#sum(int, int)
to {GET [/sum]}: There is already 'controller1' bean method
com.legion.learning.demo.Controller1#handleGet() mapped.
        at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping$MappingRegistry.validateMethodMapping(AbstractHandler
MethodMapping.java:676) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                     at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping$MappingRegistry.register(AbstractHandlerMethodMapping
.java:637) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                  at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.registerHandlerMethod(AbstractHandlerMethodMapping.ja
va:331) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                     at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping.registerHandlerMethod(RequestMappingHan
dlerMapping.java:507) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                       at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping.registerHandlerMethod(RequestMappingHan
dlerMapping.java:84) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                        at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.lambda$detectHandlerMethods$2(AbstractHandlerMethodMa
pping.java:298) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                             at java.base/java.util.LinkedHashMap.forEach(LinkedHashMap.java:721) ~[na:na]
        at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.detectHandlerMethods(AbstractHandlerMethodMapping.jav
a:296) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                      at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.processCandidateBean(AbstractHandlerMethodMapping.jav
a:265) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                      at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.initHandlerMethods(AbstractHandlerMethodMapping.java:
1223) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                        at org.springframework.web.servlet.handler.AbstractHandlerMethodMapping.afterPropertiesSet(AbstractHandlerMethodMapping.java:
1224) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                                        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping.afterPropertiesSet(RequestMappingHandle
rMapping.java:237) ~[spring-webmvc-6.2.8.jar:6.2.8]                                                                                          at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBean
Factory.java:1873) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                           at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFac
tory.java:1822) ~[spring-beans-6.2.8.jar:6.2.8]                                                                                              ... 18 common frames omitted

![[Pasted image 20250630100940.png]]
Above was the error in Postman Application testing
