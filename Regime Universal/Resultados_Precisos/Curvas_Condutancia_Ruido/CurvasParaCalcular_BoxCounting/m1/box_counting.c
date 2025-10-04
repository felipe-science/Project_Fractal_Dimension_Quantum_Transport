#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define Npontos 100000      //Numero de pontos do arquivo de dados
#define Npontos_bc 5        //Numero de pontos gerado no box-countung  
#define Lx 3                //Comprimento x da area analisada
#define Ly 3                //Comprimento y da area analisada  

int varredura(float x, float y, float l, float valoresx[Npontos], float valoresy[Npontos]);
void box_counting(float valoresx[Npontos], float valoresy[Npontos], float bc_logl[Npontos_bc], float bc_logn[Npontos_bc]);


int main()
{

    int i;
    float parabolax[Npontos], parabolay[Npontos], x, y, l;
    float valoresx[Npontos], valoresy[Npontos], bc_logl[Npontos_bc], bc_logn[Npontos_bc];
    double a=0;
    double b=0;
    int bufferLength = 1024;
    char buffer[bufferLength];

    //FILE *fp = fopen("dados_teste.dat", "r");
    FILE *fp = fopen("G_m1_beta4.dat", "r");
    if (!fp)
    {
        printf("Cant open file\n");
        return -1;
    }

    i = 0;
    while(fgets(buffer, bufferLength, fp))
    {
        //printf("%s\n", buffer);   
        if (2==sscanf(buffer, "%lf %lf", &a,&b))
        {
            //printf("a: %f   b: %f\n", a,b);
            valoresx[i] = a+0.5;
            valoresy[i] = b;
            i = i+1;

        }
    }

    fclose(fp);


    for(i = 0; i < Npontos; i++)
    {
        //printf("i = %d   valorx = %f   valory = %f\n",i,valoresx[i],valoresy[i]);
        x = (i*1.0/Npontos);
        y = sin(x);
        parabolax[i] = x;
        parabolay[i] = y;
    }
        


/*
    int teste = varredura(0.6, 0.3, 0.1, parabolax, parabolay);
    box_counting(parabolax, parabolay, bc_logl, bc_logn);
    

    for(i = 0; i < Npontos_bc; i++)
    {
        printf("%f    %f\n",bc_logl[i], bc_logn[i]);
    }


    printf("\n");
    int vt;
    vt = varredura(1.4, 2.0, 1.5, valoresx, valoresy);
    printf("teste = %d\n",vt);


    printf("\n");
    for(i = 0; i < Npontos; i++)
        printf("valorx[%d] = %f      valorx[%d] = %f\n",i,valoresx[i], i, valoresy[i]);
    printf("\n");
*/
    
    time_t begin = time(NULL);
    box_counting(valoresx, valoresy, bc_logl, bc_logn);
    time_t end = time(NULL);
    
    printf("Time = %ld s = %lf min\n", (end - begin),(end - begin)/60.0);

    return 0;
}



void box_counting(float valoresx[Npontos], float valoresy[Npontos], float bc_logl[Npontos_bc], float bc_logn[Npontos_bc])
{
    int i, j, k, nx, ny, ocupacao, contagem;
    float l, x, y;

    FILE *fd = fopen("DADOS_BC.dat","w");

    
    
    l = 0.4;
    while(l > 0.0125)
    {
        nx = (int)(Lx/l);
        ny = (int)(Ly/l);
        
        contagem=0;
        for(i = 0; i < nx; i++)
        {
            for(j = 0; j < ny; j++)
            {
                x = j*((float)Lx/nx);
                y = i*((float)Lx/ny)+3;
                
                ocupacao = varredura(x, y, l, valoresx, valoresy);
                if(ocupacao == 1)
                {
                    contagem++;
                }
            }
        }

        printf("l = %f   contagem = %d\n",l,contagem);
        
        
        fprintf(fd,"%f %f\n", log10(1/l),log10(contagem));
        
        
        l=l/2.0;
    }

    fclose(fd);
}


int varredura(float x, float y, float l, float valoresx[Npontos], float valoresy[Npontos])
{
    int i;
    float valx, valy;

    for(i = 0; i < Npontos; i++)
    {
        valx = valoresx[i];
        valy = valoresy[i];

        if(valx > x && valx < x+l)  
        {
            if(valy > y && valy < y+l)
            {
                //printf("deu certo\n");
                return 1;
            }   
        }

    }

    return 0;
}