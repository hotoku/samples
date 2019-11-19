window.addEventListener("load", function () {
    function sendData() {
        var XHR = new XMLHttpRequest();

        // FormData オブジェクトと form 要素を紐づけます
        var FD  = new FormData(form);

        // データが正常に送信された場合に行うことを定義します
        XHR.addEventListener("load", function(event) {
            console.log("sent");
            for(i of FD){
                console.log(i);
            }
        });

        // エラーが発生した場合に行うことを定義します
        XHR.addEventListener("error", function(event) {
            console.log("error");
            for(i of FD){
                console.log(i);
            }
        });

        // リクエストをセットアップします
        XHR.open("POST", "/");

        // 送信したデータは、ユーザがフォームで提供したものです
        XHR.send(FD);
    }
    
    // form 要素にアクセスしなければなりません
    var form = document.getElementById("myForm");

    // フォームの submit イベントを乗っ取ります
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        sendData();
    });
});    
