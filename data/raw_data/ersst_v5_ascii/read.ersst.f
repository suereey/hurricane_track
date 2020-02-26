      dimension isst(180,89), ierr(180,89)
      real sst(180,89), rlat(89)
      character*4 cyr

      pi=4.*atan(1.)
      do j=1,89
      rlat(j)=-88.0+(j-1)*2.0
      enddo

      open(61,file='ersst.dat',form='unformatted',access='direct',recl=180*89*4)
      open(71,file='ersst.dat.gav')

      do iy=1854,2017
      write(cyr(1:4),'(i4)') iy
      open(51,file='ersst.'//cyr//'.asc', status='old')

      mon12=12
c     if(iy.eq.2018) mon12=4
      do mon=1,mon12

      do i=1,180
      read(51,81) (isst(i,j),j=1,89)
      end do

      nrec=mon+(iy-1854)*12
      gav=0; www=0
      do i=1,180
      do j=1,89
      if(isst(i,j).gt.-900) then
      sst(i,j)=float(isst(i,j))/100.0
      gav=gav+sst(i,j)*cos(pi*rlat(j)/180.0)
      www=www+         cos(pi*rlat(j)/180.0)
      else
      sst(i,j)=-9999.0
      endif
      enddo
      enddo
      write(61,rec=nrec) sst
      
      if(iy.ge.1916) write(71,202) iy, mon, gav/www

      end do

      close(51)
      end do
   81 format (90i6)
  202 format (2i6, f10.3)

      stop
      end
