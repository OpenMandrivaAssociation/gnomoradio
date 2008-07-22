%define name	gnomoradio
%define version	0.15.1
%define release %mkrel 6

%define major	0
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	Finder and player of free (Creative Commons) music
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gnomoradio.org/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig ImageMagick
BuildRequires:	libsigc++2.0-devel gtkmm2.4-devel gconfmm2.6-devel
BuildRequires:	libxml++-devel libao-devel libvorbis-devel libogg-devel
BuildRequires:  desktop-file-utils

%description
Gnomoradio is a program that can find, fetch, share, and play music that is
freely available for sharing.  The Gnomoradio project is creating an
online network where artists can promote and share their music freely and
willingly. By eliminating many of the exclusionary tactics of the mainstream
music industry, musicians now have a chance to interact directly with their
listeners and receive valuable exposure.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --add-category="AudioVideo" \
  --add-category="Audio" \
  --add-category="Player" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS TODO
%{_bindir}/%name
%{_bindir}/rainbow-get
%{_sbindir}/rainbow-hub
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/rainbow
%{_includedir}/roboradio
%{_libdir}/*.so
#%{_libdir}/*.a
%{_libdir}/*.la

