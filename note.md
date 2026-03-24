
comfyui 提示詞、提示詞組太多了，又牽扯正負，可能還要備注參數，又excel紀錄查改好麻煩。
試試看使用，React  Flasker SQLite 來做個小程序，輔助我。 這三個工具我都沒使用經驗。

那就直接衝吧！
順序建議：
第一步：Flask 先跑起來

裝 Flask，寫一個 app.py
一個路由回傳 JSON，瀏覽器打開看到資料就算成功

第二步：SQLite 接上去

建一張 prompts 資料表
用 Flask 的路由做 CRUD

第三步：前端

先用最簡單的 HTML + fetch 呼叫你的 API
功能做完再考慮換 React

React 最後學，因為它學習曲線最陡，先把後端跑起來，前端用純 HTML 撐著，之後換 React 只是換畫面，邏輯不用動。
這樣一次學一個，不會同時爆炸。
要開始的話，先裝 Flask，pip install flask，然後把你第一個路由寫出來給我看。