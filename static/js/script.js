document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {

        const age = parseInt(document.querySelector('input[name="age"]').value);
        const bp = parseInt(document.querySelector('input[name="trestbps"]').value);
        const chol = parseInt(document.querySelector('input[name="chol"]').value);

        if (age < 1 || age > 120) {
            alert("Please enter a valid age between 1 and 120.");
            e.preventDefault();
            return;
        }

        if (bp < 50 || bp > 250) {
            alert("Please enter a valid blood pressure.");
            e.preventDefault();
            return;
        }

        if (chol < 100 || chol > 700) {
            alert("Please enter a valid cholesterol value.");
            e.preventDefault();
            return;
        }

    });

});