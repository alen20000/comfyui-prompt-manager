
const btn_show_all_data = document.querySelector('#show_all_data');
const cleaBtn = document.querySelector('#delect-display-content-btn');
const data_body = document.querySelector('#data_body');

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
