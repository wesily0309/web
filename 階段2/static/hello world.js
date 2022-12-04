//連接py檔案
const URL = '/get-coordinates'
const xhr = new XMLHttpRequest();
sender = JSON.stringify([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
xhr.open('POST', URL);
xhr.send(sender);