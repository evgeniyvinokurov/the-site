document.addEventListener("DOMContentLoaded", (event) => {
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "black";

    let size = 8;
    let max = 30;
    let xmax = 20;
    let busy = [];
    let ended = [];
    
    let moveLeft = false;
    let moveRight = false;


    let baseFigures = [
        [[0,1],[1,1],[0,1]],
        [[1,0],[1,1],[1,0]],
        [[0,1,0],[1,1,1]],
        [[1,1,1],[0,1,0]],
        [[1,1,1,1]],
        [[1,1,0],[0,1,1]],
        [[0,1,1],[1,1,0]],
        [[0,1],[1,1],[1,0]],
        [[1,0],[1,1],[0,1]],
        [[1,1],[1,1]]
    ];
    
    let inbusy = function(xx, yy){
        for (let f of busy) {
            for (let i in f.data) {
                for (let j in f.data[i]){
                    let x = (f.coords[0]*1 + i*1);
                    let y = (f.coords[1]*1 + j*1);

                    if (xx == x && yy == y && f.data[i][j]*1 == 1)
                        return true;
                }
            }                        
        }
        return false;
    }


    let figure = function(){

        this.clear = function(){
            for (let i in this.data){
                for (let j in this.data[i]){
                    let x = (this.coords[0]*1 + i*1) * size;
                    let y = (this.coords[1]*1 + j*1) * size;

                    if (this.data[i][j] == 1)
                        ctx.clearRect(x, y, size -2, size -2);
                }    
            }
        }

        this.fill = function(){
            for (let i in this.data){
                for (let j in this.data[i]){
                    let x = (this.coords[0]*1 + i*1) * size;
                    let y = (this.coords[1]*1 + j*1) * size;

                    if (this.data[i][j] == 1){
                        ctx.fillRect(x, y, size -2, size -2);
                    }
                }    
            }
        }

        this.check = function(f){
            for (let i in this.data) {
                for (let j in this.data[i]){
                    let x = (this.coords[0]*1 + i*1);
                    let y = (this.coords[1]*1 + j*1);

                    if (x > xmax) {
                        return [0,-1];
                    }

                    if (x < 0) {
                        return [0,1];
                    }

                    if ((inbusy(x, y) || y > max) && this.data[i][j]*1 == 1) {                            
                        ended.push(this);
                        busy.push(this)                          
                        return [1,-1];
                    }
                }    
            }
            return false;
        }

 
        let randomdata = baseFigures[Math.floor(Math.random() * baseFigures.length)];        
        this.data = randomdata;        
        this.coords = [Math.round(Math.random()*20), 0];

        return this;
    };    
    
    let figures = [new figure()];

    setInterval(function(){
        for (let f of figures){           
            f.clear();                        
            f.coords[1]++;  

            if (moveLeft){
                f.coords[0]--;  
                moveLeft = false;
            }
            if (moveRight){
                f.coords[0]++;  
                moveRight = false;
            }

            let diff = f.check();            
            if (diff)    
                f.coords[diff[0]] = f.coords[diff[0]] + diff[1];  
            
            f.fill();            
            for (let e of ended){
                figures.splice(e, 1);
            }

            ended = []
        }

        if (figures.length == 0) {
            figures.push(new figure());
        }   

    }, 100)

    document.addEventListener('keydown', function(event) {
        if (event.key == 'ArrowLeft') {
            moveLeft = true;
        }	  
  
        if (event.key == 'ArrowRight') {
            moveRight = true;
        }
    });
});
