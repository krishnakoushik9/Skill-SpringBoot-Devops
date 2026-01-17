import 'package:flutter/material.dart';  
  
void main() => runApp(MyApp());  
  
class MyApp extends StatelessWidget {  
  @override  
  Widget build(BuildContext context) {  
    return MaterialApp(  
      title: 'Welcome to Flutter',  
      home: Scaffold(  
        appBar: AppBar(  
          title: const Text("Welcome to Flutter UI world"),  
        ),        body: Center(  
          child: Container(  
            padding: const EdgeInsets.all(20),  
            decoration: BoxDecoration(  
              color: Colors.redAccent[100],  
              borderRadius: BorderRadius.circular(12),  
              border: Border.all(color: Colors.blue, width: 2),  
            ),            child: const Text(  
              "CMRCET",  
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),  
            ),          ),        ),      ),    );  }}




import 'package:flutter/material.dart';  
  
void main() => runApp(MyApp());  
  
class MyApp extends StatelessWidget {  
  @override  
  Widget build(BuildContext context) {  
    return MaterialApp(  
      title: 'Welcome to Flutter',  
      home: Scaffold(  
        appBar: AppBar(  
          title: const Text("Welcome to Flutter UI world"),  
        ),        body: const Center(  
          child: Text("Hello Abhi Universe"),  
        ),      ),    );  }}