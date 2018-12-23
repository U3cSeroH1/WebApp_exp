
function initMap() {
	
    // マップをどうひょじさせるのかを決定する
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,//初期ズーム度
        center: { lat: 33.232647, lng: 131.651055 },//最初にどこを映してるか
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            position: google.maps.ControlPosition.TOP_RIGHT
        },
        navigationControl: true,
        navigationControlOptions: {
            style: google.maps.NavigationControlStyle.ZOOM_PAN,
            position: google.maps.ControlPosition.TOP_LEFT
        },
        scaleControl: true,
        scaleControlOptions: {
            position: google.maps.ControlPosition.BOTTOM_LEFT
        }
    });//後半は謎




    // クリックしたら
    map.addListener('click', function(e) {
    getClickLatLng(e.latLng, map);//クリックした場所の座標とクリックした結果編集するマップを引数
    });




    //HTML上のフォームから入力した多分座標から地名？？？のところに飛ぶ
    var geocoder = new google.maps.Geocoder;
    var infowindow = new google.maps.InfoWindow;
    document.getElementById('submit1').addEventListener('click', function() {
    geocodeLatLng(geocoder, map, infowindow);
    });

    //HTML上のフォームから入力した多分座標から地名？？？のところに飛ぶ
    var geocoder = new google.maps.Geocoder;
    var infowindow = new google.maps.InfoWindow;
    document.getElementById('submit2').addEventListener('click', function() {
    geocodeAddress(geocoder, map);
    });
}


//クリックしたらピンたてたりピンをダブルクリックしたりしたら動くファンクション？？？
function getClickLatLng(latlng, map){

// 座標を表示　ほんとうにそれだけ
    document.getElementById('lat').textContent = latlng.lat();
    document.getElementById('lng').textContent = latlng.lng();

    var latlng = {
        lat : latlng.lat(),
        lng : latlng.lng()
    }


//ここに画像入れたら面白いんじゃね
    //しかし画像をさしたあとズームアウトしたら一緒にでかくなｒｊ
    var icon = new google.maps.MarkerImage('pin.png',
    new google.maps.Size(290,400),
    new google.maps.Point(0,0),
    new google.maps.Point(19,51)
    );









        if (disp('マーカーを設置しますか？') == true) {

            // マーカーを設置　それ以上でもそれ以下でもない
            var marker = new google.maps.Marker({
                position: latlng,
                map: map,
                animation: google.maps.Animation.DROP,
                //icon: icon
                draggable: true,
                title: "Drag me!"

            });
        }
        else {
            window.alert('No results found');
        }





        marker.addListener('dblclick', function () {
            //けす　　　　　↑ダブルクリック
            if (disp('マーカーを削除しますか？') == true) {

                marker.setMap(null);

            }
            else {
                window.alert('No results found');
            }


        });



        var infoWindow;//あったほうがいい


        var geocoder = new google.maps.Geocoder;
        geocoder.geocode({ 'location': latlng }, function (results, status) {
            if (status === 'OK') {
                if (results[0]) {

                    window.alert(results[0].formatted_address);

                    infoWindow = new google.maps.InfoWindow({ // 吹き出しの追加
                        content: results[0].formatted_address // 吹き出しに表示する内容
                        //ここにジオコードの結果を持ってきたかった．．．．．．
                    });

                } else {
                    window.alert('No results found');
                }
            } else {
                window.alert('Geocoder failed due to: ' + status);
            }
        });


 	marker.addListener('mouseover', function() { // マーカーをクリックしたとき
          infoWindow.open(map, marker);

          // 吹き出しの表示
    });


 	marker.addListener('mouseout', function() { // マーカーをクリックしたとき
     infoWindow.close(); // 吹き出しの表示
    });


    marker.addListener('click', function () { // マーカーをクリックしたとき


        infoWindow.open(map, marker);

        // 吹き出しの表示
    });

      // 座標の中心をずらす
      // http://syncer.jp/google-maps-javascript-api-matome/map/method/panTo/
      
	  map.panTo(latlng);


}

//--------------------------------------------------------------------------------------------------------------------------

    function ahe(){
        var hoge = ahe_form.textbox.value;  //テキストエリアの値を取得
         
        alert(""+ hoge +"が入力されました。");


    }



//なぞの関数
      function geocodeLatLng(geocoder, map, infowindow) {
        var input = document.getElementById('latlng').value;
        var latlngStr = input.split(',', 2);
        var latlng = {lat: parseFloat(latlngStr[0]), lng: parseFloat(latlngStr[1])};
        geocoder.geocode({'location': latlng}, function(results, status) {
          if (status === 'OK') {
            if (results[0]) {
              map.setZoom(16);
			  map.panTo(latlng);
              
			  //window.alert(results[0].formatted_address + 'mother fucker');


            } else {
              window.alert('No results found');
            }
          } else {
            window.alert('Geocoder failed due to: ' + status);
          }
        });
      }





//なぞの関数
      function geocodeAddress(geocoder, resultsMap) {

        var marker;

        var address = document.getElementById('address').value;
        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);

              resultsMap.setZoom(17);

                  marker = new google.maps.Marker({
                  position: results[0].geometry.location,
                  map: resultsMap,
                  animation: google.maps.Animation.DROP

              });

            //タイムアウトがしたかった

          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      }


//これつかえばなんでもOKだったりきゃんせるとかできる

function disp(quest) {

    // 「OK」時の処理開始 ＋ 確認ダイアログの表示
    if (window.confirm(quest)) {

        return true; // example_confirm.html へジャンプ

    }
    // 「OK」時の処理終了

    // 「キャンセル」時の処理開始
    else {

        return false; // 警告ダイアログを表示

    }
    // 「キャンセル」時の処理終了

}