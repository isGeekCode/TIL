# ๐ย CGColor

์์(color)์ ํด์ํ๋ ๋ฐฉ๋ฒ์ด ๋ช์๋์ด์๋ ์์ ๊ณต๊ฐ(color space)์ด ์๋,์์(color)์ ์ ์ํ๋ ์์์ ์งํฉ์๋๋ค

Color๋ ์ฝ์ด๊ทธ๋ํฝ์ค(CoreGraphics)ํ๋ ์์ํฌ์ ์ฐ๊ฒฐ๋์ด์์ด ์์ CG๊ฐ ๋ถ์์ด์.

์ด ๋ฐ์๋ CGRect, CGSize, CGPoint ๋ CG์ ๋ฐ์ดํฐํ์์ด์์. ios ์์ ๊ทธ๋ ค์ฃผ๋ ๊ฒ์ ๋ชจ๋ ์ฝ์ด๊ทธ๋ํฝ์ค ํ๋ ์์ํฌ๊ฐ ๋ด๋นํฉ๋๋ค

- ์ฝ์ด๊ทธ๋ํฝ์ค ํ๋ก๊ทธ๋๋ฐ ๊ฐ์ด๋
    
    [https://developer.apple.com/documentation/coregraphics](https://developer.apple.com/documentation/coregraphics)
    
- ์ฝ์ด๊ทธ๋ํฝ์ค ๊ฐ๋, ๋ฉ์๋ ๋ฑ
    
    [https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html)
    

 

# ๐ย UIColor

์์ ๋ฐ์ดํฐ ๋๋ ์ถ๊ฐ๋ก ์ํ๊ฐ(ํฌ๋ช๋)๋ฅผ ์ ์ฅํ๋ ๊ฐ์ฒด

์์ ๋ถ์ด์๋ UI๋ฅผ ๋ณด๋ฉด ์๋ค์ํผ NSObject๋ฅผ ์์๋ฐ์ผ๋ฉด์ UIKit ํ๋ ์์ํฌ์ ์ฐ๊ฒฐ๋์ด์์ด์

์ ํ์ ๋ฐ๋ฅด๋ฉด ๋นจ ์ฃผ ๋ธ ๊ฐ์ ๊ธฐ๋ณธ์ ์ธ ์์์ ๋ํ ์ ์๋ฅผ ์ ๊ณตํ๊ณ  ์์ต๋๋ค.

์ผ๋จ ์ด๊ฒ๋ง๋ด์๋ ํฐ ์ฐจ์ด๊ฐ ์์ด๋ณด์ฌ์. ๋๋ค ์์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ง๊ณ  ์๋ค๋ ๊ณตํต์ ์ ์๊ฒ ์ด์

# ๐ย ์ฐจ์ด์ 

- **UIColor**
    
    โ ์ฐ๋ฆฌ๊ฐ ์ ๋ง ๋ง์ด ๊ทธ๋์ ๋ค๋ฃจ์๋ UIKit ํ๋ ์์ํฌ์ ํ์ ์์, ์ฆ User Interface๋ฅผ ๋ค๋ฃจ๋ ๊ณณ์์ ์ง์ ํ๋ ์์
    
- **CGColor**
    
    โ Core Graphics ํ๋ ์์ํฌ์์ ์ฌ์ฉํ๋ ์์์ ์์๊ฐ์ ์ฌ์ฉํ  ๋ CGColor๋ก ์ง์ 
    

์ฐ๋ฆฌ๊ฐ ์์ฃผ์ฌ์ฉ ํ๋ View๋ UIView๋ผ๋ UIKitํ๋ ์์ํฌ์ ์ํ ์์๋ผ BackGroundColor๋ฅผ ์ง์ ํ  ๋ UIColor๋ก ์ง์ ํ๊ฒ์ด๊ณ 

๋ทฐ์ layer๋ CG์์ ๋ค๋ฃจ๋(๊ทธ๋ฆฌ๋) ์์๋ผ shadowColor, borderColor ๋ฑ์ ์ค๋์๋ CGColor๋ก ์ง์ ํ๋ ๊ฒ

# ๐ย ****์์

View์ ํ๋๋ฆฌ ์์์ ์ง์ ํ๋ ค๋ฉด layer.borderColor = UIColor.black.cgColor 

์ด๋ ๊ฒ ์ ๊ทผ์ ํด์ผํฉ๋๋ค. UIColor๋ก ์์ ์ง์ ํด์ฃผ๊ณ  ๊ทธ ์์์ CGColor๋ก ์ก์์ฃผ๋ ๊ฑฐ์์.

borderColor๋ CGColor๋ฅผ ์์๋ฐ๊ณ  ์๊ฑฐ๋ ์. 

โ ๋๋ฌธ์ cgColor๊ฐ ์๋๋ฉด ์๋ฌ๊ฐ ๋ฐ์ํฉ๋๋ค. 

label, Button, View ๋ชจ๋ layer๊ฐ ์๊ธฐ ๋๋ฌธ์ Border๋ฅผ ์ค ์๊ฐ ์์ต๋๋ค.