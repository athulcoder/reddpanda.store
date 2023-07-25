function openTab(event, tabName) {
    const tabContents = document.getElementsByClassName('tab-content');
    for (let i = 0; i < tabContents.length; i++) {
      tabContents[i].style.display = 'none';
    }
  
    const tabButtons = document.getElementsByClassName('tab-button');
    for (let i = 0; i < tabButtons.length; i++) {
      tabButtons[i].classList.remove('active');
    }
  
    const activeTabContent = document.getElementById(tabName);
    const activeTabButton = event.currentTarget;
    activeTabContent.style.display = 'block';
    activeTabButton.classList.add('active');
  }