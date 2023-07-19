const { exec } = require('child_process');

exec('python3 -m pip install -r requirements.txt', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error installing Python dependencies: ${error.message}`);
    return;
  }

  console.log('Python dependencies installed successfully.');

  // Now that the dependencies are installed, you can execute the main.py script.
  exec('python3 main.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing main.py: ${error.message}`);
      return;
    }

    console.log(stdout);
    console.error(stderr);
  });
});
