//! Eventy
window.addEventListener("DOMContentLoaded", function()
{
    Włączenie_Tooltipów_Bootstrap();
    Formularze_Wyświetlanie_Wartości_Range();

    window.addEventListener("scroll", Strzałka_Scroll_Przycisk);
})

//! Funkcje
function Włączenie_Tooltipów_Bootstrap()
{
    /* Włącznie tooltipów z Bootstrap 5, źródło: https://getbootstrap.com/docs/5.3/components/tooltips/#enable-tooltips. W przypadku button[data-bs-toggle="button"] bootstrap błędnie wyświetla console.error() */

    tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"], [title]')

    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
}

function Zmiana_Trybu_Motywu()
{
    /* Zmienia trybu motywu z Bootstrap 5 poprzez zmianę atrybuty "data-bs-theme" znacnzika "html". */

    Znacznik = document.querySelector("html")

    if (!Znacznik.hasAttribute("data-bs-theme") || Znacznik.getAttribute("data-bs-theme") == "light")
    {
        Znacznik.setAttribute("data-bs-theme", "dark")
    }
    else
    {
        Znacznik.setAttribute("data-bs-theme", "light")
    }
}

function Formularz_Wyświetlanie_Hasła(Selektor)
{
    /* Wyświetla zawartość pola z hasłem w formularzach. */

    var Pole = document.querySelector(Selektor);

    if (Pole.type === "password")
    {
        Pole.type = "text";
    }
    else
    {
        Pole.type = "password";
    }
}

function Strzałka_Scroll_Przycisk()
{
    /* Wyświetlanie/ukrywanie przycisku który po kliknięciu przewija stronę do samej góry. */

    if (document.documentElement.scrollTop > 50)
    {
        document.querySelector("#Przycisk_Scroll").style.display = "initial";
    }
    else
    {
        document.querySelector("#Przycisk_Scroll").style.display = "none";
    }

}

function Strzałka_Scroll()
{
    document.documentElement.scrollTop = 0;
}

var Czy_Podkreślono_Linki = false;
function Podkreślenie_Linków()
{
    /* Wymuszenie podkreślania wszytkich linków. Ta funkcja dodaje style liniowe. */

    console.log(document.querySelectorAll("a"));
    if (!Czy_Podkreślono_Linki)
    {
        document.querySelectorAll("a").forEach(x => x.style.textDecoration = "underline");
        Czy_Podkreślono_Linki = true;
    }
    else
    {
        document.querySelectorAll("a").forEach(x => x.style.textDecoration = "none");
        Czy_Podkreślono_Linki = false;
    }
}

function Formularze_Wyświetlanie_Wartości_Range()
{
    /* Wyświetlanie wartości pól typu range z formularzy. */

    var Pola_Range = document.querySelectorAll("form input[type='range']");
    Pola_Range.forEach(x => x.addEventListener("input", function()
    {
        document.querySelector(`#Wartość_Range_${x.id}`).textContent = x.value;
    }));
}