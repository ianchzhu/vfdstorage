function login() {
  // 获取输入框的值
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // 发送异步请求以获取文件内容
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "login.json", true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var data = JSON.parse(xhr.responseText);
      var users = data.users;

      // 遍历用户列表，检查输入的用户名和密码是否与任何用户匹配
      for (var i = 0; i < users.length; i++) {
        if (username === users[i].username && password === users[i].password) {
          alert("Login successful!"); // 登录成功提示
          // 这里可以添加重定向到其他页面的代码
          return;
        }
      }

      alert("Invalid username or password!"); // 登录失败提示
    }
  };
  xhr.send();
}
