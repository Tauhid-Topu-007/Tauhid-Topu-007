const fs = require('fs');
const path = require('path');

function updateReadme() {
    console.log('Updating README stats...');
    
    const readmePath = path.join(__dirname, '../README.md');
    
    if (fs.existsSync(readmePath)) {
        let content = fs.readFileSync(readmePath, 'utf8');
        
        // Update date
        const today = new Date().toLocaleDateString();
        content = content.replace(
            /Last Updated: .*?]/,
            `Last Updated: ${today}]`
        );
        
        fs.writeFileSync(readmePath, content);
        console.log('✅ README updated successfully!');
    } else {
        console.log('README.md not found');
    }
}

updateReadme();
