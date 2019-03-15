var eater_credentials = {
    login: "",
    passwd: ""
};

var enableSubmitBtn = function() {
    vm.$refs.submitButton.disabled = !(eater_credentials.login.length && eater_credentials.passwd.length);
};

var vm = null;

window.onload = function () {
    vm = new Vue({
        el: "#app",

        data: eater_credentials,
        created: function() {
            console.log('Vue instance is created');
        },
        destroyed: function() {
            console.log('Vue instance was destroyed');
        },
        watch: {
            login: enableSubmitBtn,
            passwd: enableSubmitBtn
        }
    });
}
