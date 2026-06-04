const fs = require('fs');
const path = require('path');
const https = require('https');

async function fetchGitHubStats(username) {
  return new Promise((resolve, reject) => {
    https.get(`https://api.github.com/users/${username}`, {
      headers: { 'User-Agent': 'Node.js' }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const userData = JSON.parse(data);
          resolve({
            followers: userData.followers || 0,
            following: userData.following || 0,
            publicRepos: userData.public_repos || 0
          });
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

async function updateReadme() {
  console.log('🔄 Updating README with latest stats...');
  
  try {
    const stats = await fetchGitHubStats('tauhid-topu-007');
    const readmePath = path.join(__dirname, '../README.md');
    
    if (fs.existsSync(readmePath)) {
      let content = fs.readFileSync(readmePath, 'utf8');
      
      // Update last updated date
      const today = new Date().toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
      
      // Add update marker
      const updateMarker = `\n<!-- Last updated: ${today} -->\n`;
      
      if (!content.includes('Last updated:')) {
        content += updateMarker;
      } else {
        content = content.replace(/<!-- Last updated: .*? -->/, `<!-- Last updated: ${today} -->`);
      }
      
      fs.writeFileSync(readmePath, content);
      console.log('✅ README updated successfully!');
      console.log(`📊 Stats: ${stats.followers} followers, ${stats.publicRepos} repos`);
    } else {
      console.log('❌ README.md not found!');
    }
  } catch (error) {
    console.error('❌ Error updating README:', error.message);
  }
}

updateReadme();