/*零件清單 */
const btn_show_all_data = document.querySelector('#show_all_data');
const cleaBtn = document.querySelector('#delect-display-content-btn');
const data_body = document.querySelector('#data_body');
const addBtn = document.getElementById('add_prompt-btn');


/*工具區 */

// 新增promt，打包資料成JSON物件準備送出
function _getformdata(){
    const prompt_content = document.getElementById("field_prompt_content").value;
    const prompt_class = document.getElementById('prompt_class').value;
    const comment = document.getElementById('field_prompt_comment').value;
    const is_word = document.getElementById('field_is_word').checked ? 1 : 0;

    //合成json物件
    const payload = {                   // 這裡的 Key 要跟 SQL 欄位名對齊
        "prompt": prompt_content,
        "prompt_class": prompt_class,
        "comment": comment,
        "is_word": is_word
    };

    console.log("打包完成:", payload); //測試用
    return payload;
}




btn_show_all_data.addEventListener('click', () =>{
        fetch('/get_all_prompts')
            .then(res => res.json())   // then完成後會直接給下個then， 變數res 是拋棄式的
            .then(data =>{
                const rows = data.data;
                // console.log(data); // 這裡的data是從後端回傳的json物件，裡面包含了status和data兩個屬性，data屬性是一個陣列，裡面包含了所有的prompt資料。

                let html = "";
                rows.forEach(item => {
                    //TODO 轉換映射在這

                    html +=`
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.prompt_class}</td>
                        <td>${item.prompt}</td>
                        <td>${item.comment}</td>
                    </tr>
                    `;
                    
                });

                data_body.innerHTML = html;
            });
});


cleaBtn.addEventListener('click', () =>{
    data_body.innerHTML = "";
});



addBtn.addEventListener('click', async  () =>{
    //呼叫打包
    const payload = _getformdata();  

    const response = await fetch('/add_prompt', {
        method: 'POST', // 告訴後端我要「新增」東西
        headers: { 'Content-Type': 'application/json' }, // 告訴後端這是一封 JSON 格式的包裹，這行大家都複製的
        body: JSON.stringify(payload) // 把物件轉成「字串」，不然網路傳不動
    });

});