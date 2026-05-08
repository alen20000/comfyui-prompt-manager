/*零件清單 */
const btn_show_all_data = document.querySelector('#show_all_data');
const cleaBtn = document.querySelector('#delect-display-content-btn');
const data_body = document.querySelector('#data_body');
const addBtn = document.getElementById('add_prompt-btn');
const delete_btn = document.getElementById("delete_prompt-btn")
const update_btn = document.getElementById("update_prompt-btn");
/*工具區 */

// 新增函式，打包資料成JSON物件準備送出
function _get_formdata(){
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

//刪除函式
function _delet_prompt(){
    /* 從瀏覽器ID欄位，獲得ID */
    const prompt_ID = document.getElementById("field_id").value;

    const payload = {
        "id":prompt_ID
    };
    console.log("打包完成:", payload); //測試用
    return payload;
}
// 更新內容的函式
function _update_prompt(){
    const prompt_ID = document.getElementById("field_id").value;

    const payload ={
        "id": prompt_ID,
        "prompt": document.getElementById("field_prompt_content").value,
        "prompt_class": document.getElementById('prompt_class').value,
        "comment": document.getElementById('field_prompt_comment').value,
        "is_word": document.getElementById('field_is_word').checked ? 1 : 0
    }
    console.log("打包完成:", payload); //測試用
    return payload;
}


function setFields(id, p_class, prompt, comment) {
/* 點擊資料列表後，自動往上填入表單 */

    document.getElementById("field_id").value = id;
    

    document.getElementById("prompt_class").value = p_class;
    

    document.getElementById("field_prompt_content").value = prompt;
    

    document.getElementById("field_prompt_comment").value = comment;

    console.log("已選取 ID:", id);
}
// 點擊「顯示全部」按鈕，從後端抓取資料並渲染表格
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
                    <tr onclick="setFields('${item.id}', '${item.prompt_class}', '${item.prompt}', '${item.comment}')" style="cursor: pointer;">
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

// 點擊「清空顯示」按鈕，把表格內容清空
cleaBtn.addEventListener('click', () =>{
    data_body.innerHTML = "";
});


//點擊「新增」按鈕，從表單獲取資料，打包成JSON物件，發送給後端
addBtn.addEventListener('click', async  () =>{
    //呼叫打包
    const payload = _get_formdata();  

    //向瀏覽器發請求，下面這個是瀏覽器內建的標準規範，用來跟後端溝通的API，叫做Fetch API，功能是「發出一個HTTP請求」，然後等後端回應。
    const response = await fetch('/add_prompt', {
        method: 'POST', // 告訴後端我要「新增」東西
        headers: { 'Content-Type': 'application/json' }, // 告訴後端這是一封 JSON 格式的包裹，這行大家都複製的
        body: JSON.stringify(payload) // 把物件轉成「字串」，不然網路傳不動
    });

});

//點擊「刪除」按鈕，從表單獲取ID，打包成JSON物件，發送給後端
delete_btn.addEventListener('click', 
    async ()=>{

        const payload = _delet_prompt();

        
        const response = await fetch('/delete_prompt',{
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

    }
);

//點擊「更新」按鈕，從表單獲取ID和其他欄位資料，打包成JSON物件，發送給後端
update_btn.addEventListener('click', 
    async () => {
    
        const payload = _update_prompt();

        const response = await fetch('/update_prompt',{
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
    }
);