# iOS - Setting 앱 클론



![](https://i.imgur.com/YGedQEF.png) ![](https://i.imgur.com/FK5gZGc.png)




```dart
import 'dart:math';  
  
import 'package:flutter/material.dart';  
import 'package:flutter/services.dart';  
  
void main() {  
  runApp(MyApp());  
}  
  
class MyApp extends StatelessWidget {  
  const MyApp({super.key});  
  
  @override  
  Widget build(BuildContext context) {  
    return MaterialApp(home: MainScreen());  
  }  
}  
  
class MainScreen extends StatelessWidget {  
  const MainScreen({super.key});  
  
  @override  
  Widget build(BuildContext context) {  
    return AnnotatedRegion<SystemUiOverlayStyle>(  
      value: SystemUiOverlayStyle.dark,  
      child: Scaffold(  
        body: Container(  
          color: Colors.grey[300],  
          padding: EdgeInsets.fromLTRB(  
            10,  
            MediaQuery  
                .of(context)  
                .padding  
                .top,  
            10,  
            0,  
          ),  
  
          child: Padding(  
            padding: const EdgeInsets.all(10.0),  
            child: Column(  
              spacing: 20,  
              mainAxisAlignment: MainAxisAlignment.start,  
              crossAxisAlignment: CrossAxisAlignment.start,  
              children: [  
                Text(  
                  '설정',  
                  style: TextStyle(  
                    fontSize: 30,  
                    fontWeight: FontWeight.bold,  
                    height: 1.0,  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.grey[400],  
                    width: double.infinity,  
                    height: 40,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
                    child: Row(  
                      mainAxisAlignment: MainAxisAlignment.start,  
                      children: [  
                        Icon(Icons.search, size: 30),  
                        SizedBox(width: 10),  
                        Text('검색', style: TextStyle(fontSize: 20, height: 1.0)),  
                        Spacer(),  
                        Icon(Icons.mic, size: 30),  
                      ],  
                    ),  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.white,  
                    width: double.infinity,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
                    height: 180,  
                    child: Column(  
                      mainAxisAlignment: MainAxisAlignment.start,  
                      children: [  
                        Expanded(  
                          flex: 3,  
                          child: Row(  
                            mainAxisAlignment: MainAxisAlignment.start,  
                            children: [  
                              CircleAvatar(  
                                radius: 30,  
                                backgroundColor: Colors.blue,  
                                child: Icon(  
                                  Icons.person,  
                                  color: Colors.white,  
                                  size: 35,  
                                ),  
                              ),  
  
                              SizedBox(width: 20),  
                              Column(  
                                mainAxisAlignment: MainAxisAlignment.center,  
                                crossAxisAlignment: CrossAxisAlignment.start,  
                                children: [  
                                  Text(  
                                    '홍길동',  
                                    style: TextStyle(  
                                      fontSize: 20,  
                                      fontWeight: FontWeight.bold,  
                                    ),  
                                  ),  
                                  Text(  
                                    'Apple 계정, iCloud+ 등',  
                                    style: TextStyle(fontSize: 15),  
                                  ),  
                                ],  
                              ),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
  
                        Expanded(  
                          flex: 2,  
                          child: Row(  
                            children: [  
                              Stack(  
                                clipBehavior: Clip.none,  
                                children: [  
                                  CircleAvatar(  
                                    radius: 18,  
                                    backgroundColor: Colors.green,  
                                    child: Icon(  
                                      Icons.person,  
                                      color: Colors.white,  
                                      size: 18,  
                                    ),  
                                  ),  
                                  Positioned(  
                                    left: 30,  
                                    child: CircleAvatar(  
                                      radius: 18,  
                                      backgroundColor: Colors.orange,  
                                      child: Icon(  
                                        Icons.person,  
                                        color: Colors.white,  
                                        size: 18,  
                                      ),  
                                    ),  
                                  ),  
                                ],  
                              ),  
                              SizedBox(width: 45),  
                              Text('가족', style: TextStyle(fontSize: 15)),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey[900],  
                        ),  
                        Expanded(  
                          flex: 2,  
  
                          child: Row(  
                            children: [  
                              Text('iPhone 백업 안 됨'),  
                              Spacer(),  
                              CircleAvatar(  
                                radius: 12,  
                                backgroundColor: Colors.red,  
                                child: Text(  
                                  '1',  
                                  style: TextStyle(  
                                    fontSize: 12,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              Icon(Icons.chevron_right),  
                            ],  
                          ),  
                        ),  
                      ],  
                    ),  
                  ),  
                ),  
  
                ClipRRect(  
                  borderRadius: BorderRadius.circular(10),  
                  child: Container(  
                    color: Colors.white,  
                    width: double.infinity,  
                    padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),  
  
                    height: 250,  
  
                    child: Column(  
                      children: [  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.orange,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Transform.rotate(  
                                    angle: pi / 2,  
                                    child: Icon(  
                                      Icons.flight,  
                                      color: Colors.white,  
                                    ),  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('에어플레인 모드'),  
                              Spacer(),  
                              Switch(  
                                value: false,  
                                activeTrackColor: Colors.green,  
                                onChanged: (value) {  
                                  print('test');  
                                },  
                              ),  
                            ],  
                          ),  
                        ),  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.blueAccent,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.wifi,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('Wi-Fi'),  
                              Spacer(),  
                              Text('KT-wifi 35D34-5G'),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.blueAccent,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.bluetooth,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('Bluetooth'),  
                              Spacer(),  
                              Text('켬'),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                        Divider(  
                          thickness: 0.2,  
                          indent: 80,  
                          height: 1,  
                          color: Colors.grey,  
                        ),  
                        Expanded(  
                          child: Row(  
                            children: [  
                              ClipRRect(  
                                borderRadius: BorderRadius.circular(10),  
                                child: Container(  
                                  color: Colors.green,  
                                  padding: const EdgeInsets.all(10),  
                                  child: Icon(  
                                    Icons.cell_tower,  
                                    color: Colors.white,  
                                  ),  
                                ),  
                              ),  
                              SizedBox(width: 10),  
  
                              Text('셀룰러'),  
                              Spacer(),  
                              Icon(Icons.chevron_right),  
  
                            ],  
                          ),  
                        ),  
  
                      ],  
                    ),  
                  ),  
                ),  
              ],  
            ),  
          ),  
        ),  
      ),  
    );  
  }  
}
```


