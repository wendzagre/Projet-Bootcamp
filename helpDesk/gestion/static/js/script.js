const faqs = document.querySelectorAll("question");
faqs.forEach(question =>{
    question.addEventListener('click',() => {
        question.classList.toggle('active');
    });
});