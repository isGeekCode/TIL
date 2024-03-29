# Virtual Memory - Page File Swap

 페이지 파일 스왑은 물리적인 메모리 부족 상황에서 어플리케이션의 사용하지 않는 데이터를 하드 디스크 등 다른 저장 장치에 저장하는 기술이다. 이를 통해, 현재 사용하지 않는 데이터는 하드 디스크 등 다른 저장 장치에 저장하고, 필요할 때 다시 물리적인 메모리에 불러올 수 있다.

가상 메모리는 물리 메모리 안에 따로 할당된 공간으로, 프로그램이 사용하는 메모리를 가상 메모리에 할당하고, 필요한 경우에만 물리 메모리로 로드하여 사용합니다. 이를 위해 가상 메모리는 페이지(page) 라는 고정된 크기의 블록으로 나누어져 있으며, 페이지 단위로 메모리를 할당한다.

페이징(paging)은 가상 메모리와 물리 메모리 사이에서 페이지(page) 단위로 데이터를 이동시키는 기술을 말한다. 페이징 기술은 가상 메모리에 할당된 페이지가 물리 메모리에 없을 경우, 해당 페이지를 디스크에서 물리 메모리로 로드하여 사용한다. 이를 스왑(swap)이라고도 부른다.


iOS에서 페이지 파일 스왑 기술을 사용하는 경우, 몇 가지 장단점이 있을 수 있다.

## 장점

메모리 용량 확보 : 페이지 파일 스왑을 사용하면, 물리적인 메모리 용량보다 큰 양의 데이터를 저장할 수 있다. 따라서, iOS에서 실행되는 여러 어플리케이션을 동시에 실행하거나, 더 많은 데이터를 처리할 수 있다.

어플리케이션 강제 종료 방지 : 페이지 파일 스왑을 사용하면, 메모리 부족 상황에서도 어플리케이션이 강제로 종료되지 않는다. 대신, 운영 체제가 페이지 파일 스왑을 사용하여 메모리 용량을 보완하고, 어플리케이션의 동작을 지속할 수 있다.

유연성 : 페이지 파일 스왑을 사용하면, 물리적인 메모리 용량을 보완하기 위해 여러 가지 저장 장치를 사용할 수 있다. 이는 iOS 기기의 다양한 용량 및 성능을 고려하여 메모리 용량을 확보하는 데 유리하다.

메모리 용량 관리 : 페이지 파일 스왑을 사용하면, 운영 체제가 메모리 용량을 자동으로 관리해주므로, 개발자는 메모리 용량 관리에 대한 부담을 덜 수 있다.

## 단점

성능 저하 : 페이지 파일 스왑을 사용하면, 물리적인 메모리보다 큰 양의 데이터를 저장할 수 있다. 그러나, 하드 디스크 등 다른 저장 장치에 데이터를 저장하고 다시 불러오는 과정에서 성능이 저하될 수 있다.

배터리 소모 : 페이지 파일 스왑을 사용하면, 하드 디스크 등 다른 저장 장치에 데이터를 저장하고 다시 불러오는 과정에서 배터리 소모가 증가할 수 있다.

어플리케이션 종료 시간 증가 : 페이지 파일 스왑을 사용하면, 어플리케이션을 종료하는 데 걸리는 시간이 증가할 수 있다.

하드 디스크 등 다른 저장 장치 수명 단축 : 페이지 파일 스왑을 사용하면, 하드 디스크 등 다른 저장 장치에 빈번하게 데이터를 저장하고 불러오는 과정에서 저장 장치의 수명이 단축될 수 있다.

## 직접적으로 개발자가 구현하는 것인가

iOS에서 페이지 파일 스왑은 운영 체제 수준에서 지원하는 기능이므로, 개발자가 직접 구현하는 것은 불가능하다. 

개발자는 ARC(Automatic Reference Counting) 등 iOS에서 제공하는 메모리 관리 기술을 이용하여 메모리를 할당하고 해제하는 작업을 자동으로 처리할 수 있다. 또한, iOS에서 제공하는 다양한 메모리 관리 도구를 활용하여, 메모리 누수(memory leak)와 같은 문제를 미 연에 방지할 수 있다.


페이징 스왑(paging swap)은 가상 메모리를 이용하여 물리 메모리의 한계를 극복하고, 여러 프로그램이 동시에 실행될 때 안정적인 환경을 제공한다. 따라서, 운영체제에서는 페이징 스왑을 효율적으로 관리하기 위한 다양한 기술을 제공하며, 개발자는 이를 이해하고 애플리케이션의 메모리 사용을 최적화하는 방법을 고민해야 한다.



