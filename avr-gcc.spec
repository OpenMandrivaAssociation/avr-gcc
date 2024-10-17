%define target avr
%define distsuffix edm

Name:           %{target}-gcc
Version:        4.4.3
Release:        %mkrel 1
Summary:        Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
License:        GPLv2+
URL:            https://gcc.gnu.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-core-%{version}.tar.bz2
Source1:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-g++-%{version}.tar.bz2


BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  %{target}-binutils >= 2.13, zlib-devel gawk libgmp-devel libmpfr-devel 
Requires:       %{target}-binutils >= 2.13
#Requires:       avr-libc
Conflicts:      cross-avr-gcc

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.


%package c++
Summary:        Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}
Conflicts:      cross-avr-gcc-c++

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native %{_arch}
platform.


%prep
%setup -q -c -a 1
pushd gcc-%{version}


%build
mkdir -p gcc-%{target}

ln -s gcc-%{version}/gcc gcc

pushd gcc-%{target}
#CC="%{__cc} ${RPM_OPT_FLAGS} " \

CC="%{__cc} ${RPM_OPT_FLAGS/-Werror=format-security/} " \
../gcc-%{version}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --infodir=%{_infodir} --target=%{target} --enable-languages=c,c++ \
  --disable-nls --disable-libssp --with-system-zlib \
  --enable-version-specific-runtime-libs \
  --enable-werror=no
# In general, building GCC is not smp-safe
make


popd


%install
rm -rf $RPM_BUILD_ROOT
pushd gcc-%{target}
make install DESTDIR=$RPM_BUILD_ROOT
popd
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a
# and these aren't usefull for embedded targets
rm -r $RPM_BUILD_ROOT/usr/lib/gcc/%{target}/%{version}/install-tools
rm -rf $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{version}/install-tools



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc gcc-%{version}/COPYING gcc-%{version}/COPYING.LIB
%{_bindir}
%{_bindir}/%{target}-*

/usr/lib/gcc/avr/%{version}/avr25/libgcc.a                                          
   /usr/lib/gcc/avr/%{version}/avr25/libgcov.a                                         
   /usr/lib/gcc/avr/%{version}/avr3/libgcc.a                                           
   /usr/lib/gcc/avr/%{version}/avr3/libgcov.a                                          
   /usr/lib/gcc/avr/%{version}/avr31/libgcc.a                                          
   /usr/lib/gcc/avr/%{version}/avr31/libgcov.a                                         
   /usr/lib/gcc/avr/%{version}/avr35/libgcc.a                                          
   /usr/lib/gcc/avr/%{version}/avr35/libgcov.a                                         
   /usr/lib/gcc/avr/%{version}/avr4/libgcc.a                                           
   /usr/lib/gcc/avr/%{version}/avr4/libgcov.a                                          
   /usr/lib/gcc/avr/%{version}/avr5/libgcc.a                                           
   /usr/lib/gcc/avr/%{version}/avr5/libgcov.a                                          
   /usr/lib/gcc/avr/%{version}/avr51/libgcc.a                                          
   /usr/lib/gcc/avr/%{version}/avr51/libgcov.a                                         
   /usr/lib/gcc/avr/%{version}/avr6/libgcc.a                                           
   /usr/lib/gcc/avr/%{version}/avr6/libgcov.a                                          
   /usr/lib/gcc/avr/%{version}/include-fixed/README                                    
   /usr/lib/gcc/avr/%{version}/include-fixed/limits.h                                  
   /usr/lib/gcc/avr/%{version}/include-fixed/syslimits.h                               
   /usr/lib/gcc/avr/%{version}/include/float.h                                         
   /usr/lib/gcc/avr/%{version}/include/iso646.h                                        
   /usr/lib/gcc/avr/%{version}/include/stdarg.h                                        
   /usr/lib/gcc/avr/%{version}/include/stdbool.h                                       
   /usr/lib/gcc/avr/%{version}/include/stddef.h                                        
   /usr/lib/gcc/avr/%{version}/include/stdfix.h                                        
   /usr/lib/gcc/avr/%{version}/include/tgmath.h                                        
   /usr/lib/gcc/avr/%{version}/include/unwind.h                                        
   /usr/lib/gcc/avr/%{version}/include/varargs.h                                       
   /usr/lib/gcc/avr/%{version}/libgcc.a                                                
   /usr/lib/gcc/avr/%{version}/libgcov.a                                               
   /usr/libexec/gcc/avr/%{version}/cc1                                                             
   /usr/libexec/gcc/avr/%{version}/collect2                                            
   /usr/libexec/gcc/avr/%{version}/install-tools/fixinc.sh                             
   /usr/libexec/gcc/avr/%{version}/install-tools/fixincl                               
   /usr/libexec/gcc/avr/%{version}/install-tools/mkheaders                             
   /usr/libexec/gcc/avr/%{version}/install-tools/mkinstalldirs                         
   /usr/share/man/man1/avr-cpp.1.lzma                                             
   /usr/share/man/man1/avr-g++.1.lzma                                             
   /usr/share/man/man1/avr-gcc.1.lzma                                             
   /usr/share/man/man1/avr-gcov.1.lzma   
%exclude %{_bindir}/%{target}-?++
%exclude /usr/libexec/gcc/avr/%{version}/cc1plus  

%files c++
%defattr(-,root,root,-)
%{_bindir}/%{target}-?++
   /usr/libexec/gcc/avr/%{version}/cc1plus                                                                                      
   
                                            




