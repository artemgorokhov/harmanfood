/*jslint browser */
/*global window */

window.onload = function () {
    "use strict";

    var vm = null;

    var eater_credentials = {
        login: "",
        passwd: ""
    };

    var enableSubmitBtn = function () {
        vm.$refs.submitButton.disabled = form_is_invalid();
    };

    var form_is_invalid = function() {
        return !(eater_credentials.login.length && eater_credentials.passwd.length);
    }

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
        },

        methods: {
            submit: function(){
                console.log('Submit button clicked');
                if (!form_is_invalid()) {
                    axios.post('/api/login', {
                        username: eater_credentials.login,
                        password: eater_credentials.passwd
                    })
                    .then(function(response){
                        if (!response.data.hasOwnProperty('result')) {
                            console.log("Response without result...");
                        }
                        if (response.data.result == 'success') {
                            console.log("All right, redirecting to home page");
                            window.location.href = '/';
                        }
                        else {
                            console.log("Wrong credentials!");
                        }
                    })
                    .catch(function(error){
                        console.log('Error: ' + error);
                    })
                }
            }
        }
    });
};
