// Custom analytics tracking for profile visits
(function() {
  const startTime = new Date();
  
  window.addEventListener('load', function() {
    const loadTime = new Date() - startTime;
    console.log(`📊 Page loaded in ${loadTime}ms`);
    
    // Track profile visit
    fetch('https://api.github.com/users/tauhid-topu-007', {
      method: 'GET',
      headers: {
        'Accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      console.log(`👤 Profile: ${data.name}`);
      console.log(`📈 Followers: ${data.followers}`);
    })
    .catch(error => console.error('Analytics error:', error));
  });
})();