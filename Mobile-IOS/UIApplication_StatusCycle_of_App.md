# UIApplication - AppDelegate - App's Status / App's Life-Cycle

- UIApplication: 애플리케이션의 라이프 사이클을 관리하는 싱글톤 클래스

화면을 터치하여 앱을 실행시키면 UIApplication이라는 클래스에  오프젝트 하나가 생긴다.
자신의 이벤트를 대행해줄  AppDelegate라는 오브젝트를 만든다.

AppDelegate라는 Object는 개발자가 직접 만들어가는 클래스이다. 
Application의 시동, 종료, Background,Foreground, in-active, active 상태로 다녀오는 것을 관리한다. 

가장먼저 하는 일은 window을 만드는 것이다.
iOS에서는 기본적으로 Single-window이다. 
`하나의 window가 앱 전체를 채우고 있고, 앱을 종료하면 window가 종료된다.`

App에서 사용하는 여러 data들은 AppDelegate가 관리한다. 이는 AppDelegate가 UIApplication으로 부터 앱의 시동과 종료등에 중요한 역할을 위임받고 있고, Singleton에 준하는 Object이기 때문이다. 

아이폰에서 주 화면에 현재 앱이 얼마만큼 점유하고 있느냐에 따라 앱의 상태가 달라진다. 


## Not Running
앱이 시작되지않은상태


## Foregound
앱이 화면을 점유하고 있는 상태이다. 


- InActive
Active상태로 들어오거나 나갈때 잠시 거치는 상태이다. 앱을 사용중에 푸시가 오거나 전화가 온다면 갑자기 잠시 화면이 바뀔때가 있다. 이때가 바로 이 상태이다. 

- Active
앱이 돌아가고 일반 적인 상태라고 생각하면 된다. 

## Background
앱이 화면을 점유하고 있지않은 상태이다. 화면에 보이지는 않지만 앱은 살아있다.
약간의 차이에 따라 아래 두가지로 나뉘어진다. 

- Running
여전이 앱은 돌아가고 있는 상태이다. 이 상태는 잠시 들어온 것일 수도 있고 여기에 있다가 Suspend상태로 넘어갈 수도 있다.
만약 앱이 실행중이다가 다른 앱의 푸시를 누르거나 전화를 하게 되면 전환되어 백그라운드에서 돌고 있게 된다. 이 시간이 길게 유지되지는 않는다. 약15분정도 뒤에는 Apple에서 아이폰의 CPU와 배터리를 위해 자동으로 앱을 suspend처리한다. 

예를 들어 백그라운드에서 음악을 실행하거나, 걸어온 길을 트래킹 하는 등의 동작이라고 볼수 있따.

- Suspend
 백그라운드 상태에서 활동을 멈춘 상태. 빠른 재실행을 위하여 메모리에 적재된 상태지만 실질적으로 동작하고 있지는 않다. 메모리가 부족할때 비로소 시스템이 강제종료하게 된다.
