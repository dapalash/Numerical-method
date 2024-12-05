clc;
clear all;
%format short
xl(1)=input('Enter 1st initial value: ');
xu(1)=input('Enter 2nd initial value: ');
e=input('Enter desired percentage relative error: ');
d=input('Enter number of iterations: ');
%fxl(1)=exp(-xl(1))-(2*(xl(1)^3))-xl(1)+10;
%fxu(1)=exp(-xu(1))-(2*(xu(1)^3))-xu(1)+10;
fxl(1)=(667.38/xl(1))*(1-exp(-0.146843*xl(1)))-40;
fxu(1)=(667.38/xu(1))*(1-exp(-0.146843*xu(1)))-40;
if fxl(1)*fxu(1)<0
    for i=1:d
        xc(i)=(xl(i)+xu(i))/2;
        j(i)=i;
        %fxl(i)=exp(-xl(i))-(2*(xl(i)^3))-xl(i)+10;
        %fxu(i)=exp(-xu(i))-(2*(xu(i)^3))-xu(i)+10;
        %fxc(i)=exp(-xc(i))-(2*(xc(i)^3))-xc(i)+10;
        fxl(i)=(667.38/xl(i))*(1-exp(-0.146843*xl(i)))-40;
        fxu(i)=(667.38/xu(i))*(1-exp(-0.146843*xu(i)))-40;
        fxc(i)=(667.38/xc(i))*(1-exp(-0.146843*xc(i)))-40;
        if i>1
            er(i)=((xc(i)-xc(i-1))/xc(i))*100;
        end
        if i>1 && abs(er(i))<e
            break 
            else if fxc(i)==0
                break
                end
        end
        if fxc(i)>0 && fxl(i)>0
            xl(i+1)=xc(i);
            xu(i+1)=xu(i);
        else if fxc(i)>0 && fxu(i)>0
                xu(i+1)=xc(i);
                xl(i+1)=xl(i);
            else if fxc(i)<0 && fxl(i)<0
                    xl(i+1)=xc(i);
                    xu(i+1)=xu(i);
                else if fxc(i)<0 && fxu(i)<0
                        xu(i+1)=xc(i);
                        xl(i+1)=xl(i);
                    %else if fxc(i)==0
                     %       xl(i+1)=xl(i);
                      %      xu(i+1)=xu(i);
                     %       display(xc(i))
                     %       break
                        %end
                    end
                end
            end
        end
        
    end
else if fxl(1)*fxu(1)>0
        display('wrong initial input')
    else if fxl(1)*fxu(1)==0
            if fxl(1)==0
                xc(1)=xl(1);
            else if fxu(1)==0
                    xc(1)=xu(1);
                end
            end
        end
    end
end

out=[j' xl' xu' fxl' fxu' xc' fxc' er']
fprintf('The root of the equation is: %2.15f\n', xc(i))



q=0;
figure(1)
clf
axis off
axis ij
%xlim([0 100])
%ylim([0 100])
line([0 100],[0 0],'color','k','linewidth',1)
    text(1,2,'Iteration no.','fontsize', 10)
    text(9.8,2,'1st initial value','fontsize', 10)
    text(20.5,2,'2nd initial value','fontsize', 10)
    text(31,2,'Function value of x_l','fontsize', 10)
    text(45,2,'Function value of x_u','fontsize', 10)
    text(59.7,2,'Average value','fontsize', 10)
    text(71.5,2,'Function value of x_c','fontsize', 10)
    text(85.5,2,'Percentage relative error','fontsize', 10)
    %line([0 100],[5 5],'color','k','linewidth',1)
    text(4,6,'i','fontsize', 10)
    text(13,6,'x_l','fontsize', 10)
    text(24,6,'x_u','fontsize', 10)
    text(35,6,'f(x_l)','fontsize', 10)
    text(49,6,'f(x_u)','fontsize', 10)
    text(63.4,6,'x_c','fontsize', 10)
    text(75.5,6,'f(x_c)','fontsize', 10)
    text(91.5,6,'e%','fontsize', 10)
    for p=1:i
        if p==1
            q=q+8;
    %        q=q+5;
        else q=q+2;
        end
        line([0 100],[q q],'color','k','linewidth',1)
        q=q+2;
        text(3.8,q,sprintf('%d',j(p)))
        text(9.8,q,sprintf('%1.10f',xl(p)))
        text(20.3,q,sprintf('%1.10f',xu(p)))
        text(30.3,q,sprintf('%1.10f',fxl(p)))
        text(43.8,q,sprintf('%1.10f',fxu(p)))
        text(59.5,q,sprintf('%1.10f',xc(p)))
        text(70.7,q,sprintf('%1.10f',fxc(p)))
        if p>1
        text(88,q,sprintf('%1.10f',er(p)))
        else text(88,q,'N/A')
        end
    end
    line([0 100],[q+2 q+2],'color','k','linewidth',1)
    line([0 0],[0 q+2],'color','k','linewidth',1)
    line([8 8],[0 q+2],'color','k','linewidth',1)
    line([19 19],[0 q+2],'color','k','linewidth',1)
    line([29.5 29.5],[0 q+2],'color','k','linewidth',1)
    line([43 43],[0 q+2],'color','k','linewidth',1)
    line([57 57],[0 q+2],'color','k','linewidth',1)
    line([70 70],[0 q+2],'color','k','linewidth',1)
    line([84 84],[0 q+2],'color','k','linewidth',1)
    line([100 100],[0 q+2],'color','k','linewidth',1)
    title('Bisection method')
    text(40, q+4, sprintf('The root of the equation is: %1.15f',xc(i)),'fontsize',10)
    %xlabel('The root of the equation is: ')