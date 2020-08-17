function my_post() {
        const input_data = document.getElementById('110').value;
        if (input_data == null || input_data == "") {
            alert("请输入留言！");
        } else {
            alert("提交成功！")
        }
    }