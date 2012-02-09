%ifarch x86_64
%define __lib lib64
%else
%define __lib lib
%endif

Summary: A SIMD-accelerated JPEG codec which provides both the libjpeg and TurboJPEG APIs
Name: libjpeg-turbo
Version: 1.1.90
Vendor: The libjpeg-turbo Project
URL: http://www.libjpeg-turbo.org
Group: System Environment/Libraries
#-->Source0: http://prdownloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz
Release: 20120208
License: BSD-style
BuildRoot: %{_blddir}/%{name}-buildroot-%{version}-%{release}
Prereq: /sbin/ldconfig
Provides: %{name} = %{version}-%{release}, turbojpeg = 2.00
Obsoletes: turbojpeg

%description
libjpeg-turbo is a derivative of libjpeg which uses SIMD instructions (MMX,
SSE2, etc.) to accelerate baseline JPEG compression and decompression on x86
and x86-64 systems.  On such systems, libjpeg-turbo is generally 2-4x as fast
as the unmodified version of libjpeg, all else being equal.  libjpeg-turbo also
includes a wrapper library which implements the TurboJPEG API used by VirtualGL
and TurboVNC.

libjpeg-turbo was originally based on libjpeg/SIMD by Miyasaka Masaru, but
the TigerVNC and VirtualGL projects made numerous enhancements to the codec in
2009, including improved support for Mac OS X, 64-bit support, support for
32-bit and big endian pixel formats (RGBX, XBGR, etc.), accelerated Huffman
encoding/decoding, and various bug fixes.  The goal was to produce a fully open
source codec that could replace the partially closed source TurboJPEG/IPP codec
used by VirtualGL and TurboVNC.  libjpeg-turbo generally performs in the range
of 80-120% of TurboJPEG/IPP.  It is faster in some areas but slower in others.

In early 2010, libjpeg-turbo spun off into its own independent project, with
the goal of making high-speed JPEG compression/decompression technology
available to a broader range of users and developers.

#-->%prep
#-->%setup -q

#-->%build
#-->./configure libdir=/opt/%{name}/%{__lib} mandir=/opt/%{name}/man JPEG_LIB_VERSION=62 SO_MAJOR_VERSION=62 SO_MINOR_VERSION=0 --with-pic 
#-->make DESTDIR=$RPM_BUILD_ROOT libdir=/opt/%{name}/%{__lib} mandir=/opt/%{name}/man

%install

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT libdir=/opt/%{name}/%{__lib} mandir=/opt/%{name}/man
rm -f $RPM_BUILD_ROOT/opt/%{name}/%{__lib}/*.la
mkdir -p $RPM_BUILD_ROOT/usr/%{__lib}
mv $RPM_BUILD_ROOT/opt/%{name}/%{__lib}/libturbojpeg.* $RPM_BUILD_ROOT/usr/%{__lib}
/sbin/ldconfig -n $RPM_BUILD_ROOT/opt/%{name}/%{__lib}
/sbin/ldconfig -n $RPM_BUILD_ROOT/usr/%{__lib}
mkdir -p $RPM_BUILD_ROOT/usr/include
mv $RPM_BUILD_ROOT/opt/%{name}/include/turbojpeg.h $RPM_BUILD_ROOT/usr/include
ln -fs /usr/include/turbojpeg.h $RPM_BUILD_ROOT/opt/%{name}/include/
ln -fs /usr/%{__lib}/libturbojpeg.a $RPM_BUILD_ROOT/opt/%{name}/%{__lib}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{_srcdir}/README-turbo.txt %{_srcdir}/README %{_srcdir}/libjpeg.txt %{_srcdir}/usage.txt
%dir /opt/%{name}
%dir /opt/%{name}/bin
/opt/%{name}/bin/cjpeg
/opt/%{name}/bin/djpeg
/opt/%{name}/bin/jpegtran
/opt/%{name}/bin/tjbench
/opt/%{name}/bin/rdjpgcom
/opt/%{name}/bin/wrjpgcom
%dir /opt/%{name}/%{__lib}
%ifarch x86_64
%else
/opt/%{name}/lib32
%endif
/opt/%{name}/%{__lib}/libjpeg.so.62.0.0
/opt/%{name}/%{__lib}/libjpeg.so.62
/opt/%{name}/%{__lib}/libjpeg.so
/opt/%{name}/%{__lib}/libjpeg.a
/opt/%{name}/%{__lib}/libturbojpeg.a
/usr/%{__lib}/libturbojpeg.so
/usr/%{__lib}/libturbojpeg.a
/usr/include/turbojpeg.h
%dir /opt/%{name}/include
/opt/%{name}/include/jconfig.h
/opt/%{name}/include/jerror.h
/opt/%{name}/include/jmorecfg.h
/opt/%{name}/include/jpeglib.h
/opt/%{name}/include/turbojpeg.h
%dir /opt/%{name}/man
%dir /opt/%{name}/man/man1
/opt/%{name}/man/man1/cjpeg.1*
/opt/%{name}/man/man1/djpeg.1*
/opt/%{name}/man/man1/jpegtran.1*
/opt/%{name}/man/man1/rdjpgcom.1*
/opt/%{name}/man/man1/wrjpgcom.1*



%changelog
