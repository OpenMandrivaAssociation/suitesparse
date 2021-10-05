%define atlaslibs -lblas -llapack
# Version found in <libname>/Doc/ChangeLog
%define amd_version 2.4.0
%define amd_version_major 2
%define amd_packagename %mklibname amd %{amd_version_major}
%define btf_version 1.2.0
%define btf_version_major 1
%define btf_packagename %mklibname btf %{btf_version_major}
%define camd_version 2.4.0
%define camd_version_major 2
%define camd_packagename %mklibname camd %{camd_version_major}
%define ccolamd_version 2.9.0
%define ccolamd_version_major 2
%define ccolamd_packagename %mklibname ccolamd %{ccolamd_version_major}
%define cholmod_version 3.0.1
%define cholmod_version_major 3
%define cholmod_packagename %mklibname cholmod %{cholmod_version_major}
%define colamd_version 2.9.0
%define colamd_version_major 2
%define colamd_packagename %mklibname colamd %{colamd_version_major}
#%%define csparse_version 3.1.3
#%%define csparse_version_major 3
#%%define csparse_packagename %mklibname csparse %{csparse_version_major}
%define cxsparse_version 3.1.3
%define cxsparse_version_major 3
%define cxsparse_packagename %mklibname cxsparse %{cxsparse_version_major}
%define klu_version 1.3.0
%define klu_version_major 1
%define klu_packagename %mklibname klu %{klu_version_major}
%define ldl_version 2.2.0
%define ldl_version_major 2
%define ldl_packagename %mklibname ldl %{ldl_version_major}
%define umfpack_version 5.7.0
%define umfpack_version_major 5
%define umfpack_packagename %mklibname umfpack %{umfpack_version_major}
%define spqr_version 1.3.3
%define spqr_version_major 1
%define spqr_packagename %mklibname spqr %{spqr_version_major}
%define rbio_version 2.2.0
%define rbio_version_major 2
%define rbio_packagename %mklibname rbio %{rbio_version_major}
# Version found in README.txt
%define suitesparseconfig_version 4.3.1
%define suitesparseconfig_version_major 4
%define suitesparseconfig_packagename %mklibname suitesparseconfig %{suitesparseconfig_version_major}
### CHOLMOD can also be compiled to use the METIS library, but it is not
### used here because its licensing terms exclude it from Mageia.
### To compile with METIS, define enable_metis as 1 below.
%define enable_metis 0
### CXSparse is a superset of CSparse, and the two share common header
### names, so it does not make sense to build both. CXSparse is built
### by default, but CSparse can be built instead by defining
### enable_csparse as 1 below.
#%%define enable_csparse 0

Name:           suitesparse
Version:        4.4.6
Release:        1
Summary:        A collection of sparse matrix libraries

Group:          Development/C
License:        LGPLv2+ and GPLv2+
URL:            http://faculty.cse.tamu.edu/davis/suitesparse.html
Source0:        http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-%{version}.tar.gz

BuildRequires:  blas-devel
BuildRequires:  lapack-devel
BuildRequires:  tbb-devel
Requires:       %{amd_packagename}
Requires:       %{btf_packagename}
Requires:       %{camd_packagename}
Requires:       %{colamd_packagename}
Requires:       %{ccolamd_packagename}
Requires:       %{cholmod_packagename}
Requires:       %{cxsparse_packagename}
Requires:       %{klu_packagename}
Requires:       %{ldl_packagename}
Requires:       %{spqr_packagename}
Requires:       %{suitesparseconfig_packagename}
Requires:       %{umfpack_packagename}
Requires:       %{rbio_packagename}

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.  The package includes the following libraries:
  AMD                 approximate minimum degree ordering
  BTF                 permutation to block triangular form
  CAMD                constrained approximate minimum degree ordering
  COLAMD              column approximate minimum degree ordering
  CCOLAMD             constrained column approximate minimum degree ordering
  CHOLMOD             sparse Cholesky factorization
  CSparse             a concise sparse matrix package
  CXSparse            int/long/real/complex version of CSparse
  KLU                 sparse LU factorization, BLAS-free
  LDL                 a simple LDL factorization
  SQPR                a multithread, multifrontal, rank-revealing sparse QR
                      factorization method
  UMFPACK             sparse LU factorization, with the BLAS
  SuiteSparse_config  configuration file for all the above packages.
  RBio                read/write files in Rutherford/Boeing format


%package devel
Summary:        Development headers for SuiteSparse
Group:          Development/C
Requires:       suitesparse
Provides:       suitesparse-common-devel = %{version}-%{release}
Obsoletes:      suitesparse-common-devel < 4.2.1-10

Provides:       amd-devel = %{version}-%{release}
Provides:       %{mklibname -d amd} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d amd} < 1:2.3.1-10

Provides:       btf-devel = %{version}-%{release}

Provides:       amd-devel = %{version}-%{release}
Provides:       %{mklibname -d camd} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d camd} < 1:2.3.1-10

Provides:       ccolamd-devel = %{version}-%{release}
Provides:       %{mklibname -d ccolamd} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d ccolamd} < 1:2.8.0-10

Provides:       cholmod-devel = %{version}-%{release}
Provides:       %{mklibname -d cholmod} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d cholmod} < 1:2.1.2-10

Provides:       colamd-devel = %{version}-%{release}
Provides:       %{mklibname -d colamd} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d colamd} < 1:2.8.0-10

#%%if 0%{?enable_csparse:0}
#Provides:       %{mklibname -d csparse} = %{version}-%{release}
#Obsoletes:      %{mklibname -d csparse} < %{version}-%{release}
#%%endif
Provides:       cxsparse-devel = %{version}-%{release}
Provides:       %{mklibname -d cxsparse} = 1:%{version}-%{release}
Obsoletes:      %{mklibname -d cxsparse} < 1:3.1.3-10

Provides:       klu-devel = %{version}-%{release}

Provides:       ldl-devel = %{version}-%{release}

Provides:       umfpack-devel = 5.6.1-5
Provides:       %{mklibname -d umfpack} = 1:5.6.1-5
Obsoletes:      %{mklibname -d umfpack} < 1:5.6.1-10

Provides:       libspqr-devel = %{version}-%{release}

Provides:       librbio-devel = %{version}-%{release}

%description devel
The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.


%package doc
Summary:        Documentation files for SuiteSparse
Group:          Development/C
BuildArch:      noarch

%description doc
This package contains documentation files for %{name}.


%package -n %{suitesparseconfig_packagename}
Summary:	Configuration file for SuiteSparse packages
Group:		Development/C

%description -n %{suitesparseconfig_packagename}
SuiteSparse_config provides a configuration header file needed by most of 
the other packages in SuiteSparse.

%package -n %{amd_packagename}
Summary:	Routines for permuting sparse matricies prior to factorization
Group:		Development/C
Provides:   %{mklibname amd 2.3.1} = 0:2.3.1-5
Obsoletes:  %{mklibname amd 2.3.1} < 0:2.3.1-5
Provides:   %{mklibname amd 2.2.2} = 0:2.2.2-5
Obsoletes:  %{mklibname amd 2.2.2} < 0:2.2.2-5

%description -n %{amd_packagename}
AMD provides a set of routines for permuting sparse matricies prior to
Cholesky factorization (or LU factorization with diagonal pivoting).

%package -n %{btf_packagename}
Summary:	Routines for permuting sparse matricies to block triangular form
Group:		Development/C

%description -n %{btf_packagename}
BTF is a software package for permuting a matrix into block upper triangular
form.  It includes a maximum transversal algorithm, which finds a permutation
of a square or rectangular matrix so that it has a zero-free diagonal (if one
exists); otherwise, it finds a maximal matching which maximizes the number of
nonzeros on the diagonal.  The package also includes a method for finding the
strongly connected components of a graph.  These two methods together give the
permutation to block upper triangular form.

%package -n %{camd_packagename}
Summary:	Routines for permuting sparse matricies prior to factorization
Group:		Development/C
Provides:   %{mklibname camd 2.3.1} = 0:2.3.1-5
Obsoletes:  %{mklibname camd 2.3.1} < 0:2.3.1-5
Provides:   %{mklibname camd 2.2.2} = 0:2.2.2-5
Obsoletes:  %{mklibname camd 2.2.2} < 0:2.2.2-5

%description -n %{camd_packagename}
CAMD provides a set of routines for permuting sparse matricies prior
to factorization.

%package -n %{ccolamd_packagename}
Summary:	Routines for computing column approximate minimum degree ordering
Group:		Development/C
Provides:   %{mklibname ccolamd 2.8.0} = 0:2.8.0-5
Obsoletes:  %{mklibname ccolamd 2.8.0} < 0:2.8.0-5
Provides:   %{mklibname ccolamd 2.7.3} = 0:2.7.3-5
Obsoletes:  %{mklibname ccolamd 2.7.3} < 0:2.7.3-5

%description -n %{ccolamd_packagename}
The CCOLAMD column approximate minimum degree ordering algorithm computes
a permutation vector P such that the LU factorization of A (:,P)
tends to be sparser than that of A.  The Cholesky factorization of
(A (:,P))'*(A (:,P)) will also tend to be sparser than that of A'*A.

%package -n %{cholmod_packagename}
Summary:	Routines for factorizing sparse symmetric positive definite matricies
Group:		Development/C
Provides:   %{mklibname cholmod 2.0.1} = 0:2.0.1-5
Obsoletes:  %{mklibname cholmod 2.0.1} < 0:2.0.1-5
Provides:   %{mklibname cholmod 1.7.3} = 0:1.7.3-5
Obsoletes:  %{mklibname cholmod 1.7.3} < 0:1.7.3-5

%description -n %{cholmod_packagename}
CHOLMOD is a set of routines for factorizing sparse symmetric positive
definite matrices of the form A or AA', updating/downdating a sparse
Cholesky factorization, solving linear systems, updating/downdating
the solution to the triangular system Lx=b, and many other sparse
matrix functions for both symmetric and unsymmetric matrices.  Its
supernodal Cholesky factorization relies on LAPACK and the Level-3
BLAS, and obtains a substantial fraction of the peak performance of
the BLAS.  Both real and complex matrices are supported.

%package -n %{colamd_packagename}
Summary:	Routines for computing column approximate minimum degree ordering
Group:		Development/C
Provides:   %{mklibname colamd 2.8.0} = 0:2.8.0-5
Obsoletes:  %{mklibname colamd 2.8.0} < 0:2.8.0-5
Provides:   %{mklibname colamd 2.7.3} = 0:2.7.3-5
Obsoletes:  %{mklibname colamd 2.7.3} < 0:2.7.3-5

%description -n %{colamd_packagename}
The COLAMD column approximate minimum degree ordering algorithm computes
a permutation vector P such that the LU factorization of A (:,P)
tends to be sparser than that of A.  The Cholesky factorization of
(A (:,P))'*(A (:,P)) will also tend to be sparser than that of A'*A.

#%%if 0%{?enable_csparse:0}
#%%package -n %{csparse packagename}
#Summary:	
#Group:		Development/C
#Obsoletes:  %{mklibname csparse} < %{version}-%{release}
#Provides:   %{mklibname csparse} = %{version}-%{release}

#%%description -n %{csparse_packagename}

#%%endif

%package -n %{cxsparse_packagename}
Summary:	Direct methods for sparse linear systems
Group:		Development/C
Provides:   %{mklibname cxsparse 3.1.1} = 0:3.1.1-5
Obsoletes:  %{mklibname cxsparse 3.1.1} < 0:3.1.1-5
Provides:   %{mklibname cxsparse 2.2.5} = 0:2.2.5-5
Obsoletes:  %{mklibname cxsparse 2.2.5} < 0:2.2.5-5

%description -n %{cxsparse_packagename}
CSparse is a package of direct methods for sparse linear systems written
to complement the book "Direct Methods for Sparse Linear Systems", by
Timothy A. Davis. The algorithms in CSparse have been chosen with 
five goals in mind:

(1) they must embody much of the theory behind sparse matrix algorithms,
(2) they must be either asymptotically optimal in their run time and memory
    usage or be fast in practice,
(3) they must be concise so as to be easily understood and short enough to
    print in the book,
(4) they must cover a wide spectrum of matrix operations, and
(5) they must be accurate and robust.

The focus is on direct methods; iterative methods and solvers for
eigenvalue problems are beyond the scope of this package.

CXSparse is a version of CSparse that operates on both real and complex
matrices, using either int or UF_long integers.

%package -n %{klu_packagename}
Summary:	Sparse LU factorization, for circuit simulation
Group:		Development/C

%description -n %{klu_packagename}
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation.

%package -n %{ldl_packagename}
Summary:	A consise sparse Cholesky factorization package
Group:		Development/C

%description -n %{ldl_packagename}
LDL is a set of concise routines for factorizing symmetric positive-definite 
sparse matrices, with some applicability to symmetric indefinite matrices. 
Its primary purpose is to illustrate much of the basic theory of sparse matrix 
algorithms in as concise a code as possible, including an elegant new method 
of sparse symmetric factorization that computes the factorization row-by-row 
but stores it column-by-column. The entire symbolic and numeric factorization 
consists of a total of only 49 lines of code. The package is written in C,
and includes a MATLAB interface. 

%package -n %{umfpack_packagename}
Summary:	Routines for solving unsymmetric sparse linear systems
Group:		Development/C
# 5.6.1-3 is a tricky number to avoid using an epoch as old umfpack packages has a
# higher version than SuiteSparse
Provides:   %{mklibname umfpack 5.6.1} = 5.6.1-5
Obsoletes:  %{mklibname umfpack 5.6.1} < 5.6.1-5
Provides:   %{mklibname umfpack 5.5.1} = 0:5.5.1-5
Obsoletes:  %{mklibname umfpack 5.5.1} < 0:5.5.1-5
Provides:   %{mklibname umfpack 5.4.0} = 0:5.4.0-5
Obsoletes:  %{mklibname umfpack 5.4.0} < 0:5.4.0-5

%description -n %{umfpack_packagename}
UMFPACK provides a set of routines for solving unsymmetric sparse
linear systems Ax=b using the Unsymmetric MultiFrontal method. It is
written in ANSI/ISO C. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack"; it is not "You Em Ef Pack".

%package -n %{spqr_packagename}
Summary:	Multithreaded multifrontal sparse QR factorization
Group:		Development/C

%description -n %{spqr_packagename}
SuiteSparseQR is an implementation of the multifrontal sparse QR factorization
method. Parallelism is exploited both in the BLAS and across different frontal
matrices using Intel's Threading Building Blocks, a shared-memory programming
model for modern multicore architectures. It can obtain a substantial fraction
of the theoretical peak performance of a multicore computer. The package is
written in C++ with user interfaces for MATLAB, C, and C++.

%package -n %{rbio_packagename}
Summary:	MATLAB toolbox for reading/writing sparse matrices in Rutherford/Boeing
Group:		Development/C

%description -n %{rbio_packagename}
RBio - MATLAB toolbox for reading/writing sparse matrices in the 
Rutherford/Boeing format, and for reading/writing problems in the UF Sparse 
Matrix Collection from/to a set of files in a directory. 
Version 2.0 is written in C. Older versions are in Fortran. 

%prep
%autosetup -n SuiteSparse -p1

%build

mkdir -p Doc/{AMD,BTF,CAMD,CCOLAMD,CHOLMOD,COLAMD,KLU,LDL,UMFPACK,SPQR,RBio} Lib Include

# SuiteSparse_config needs to come first
pushd SuiteSparse_config
  %make_build CFLAGS="%{optflags} -fPIC"
  ar x libsuitesparseconfig.a
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libsuitesparseconfig.so.%{suitesparseconfig_version_major} -lm -o \
        libsuitesparseconfig.so.%{suitesparseconfig_version} ../SuiteSparse_config/*.o
    %__ln_s -f libsuitesparseconfig.so.%{suitesparseconfig_version} libsuitesparseconfig.so.%{suitesparseconfig_version_major}
    %__ln_s -f libsuitesparseconfig.so.%{suitesparseconfig_version} libsuitesparseconfig.so
    cp -p ../SuiteSparse_config/*.a ./
  popd
  cp -p *.h ../Include
popd

pushd AMD
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libamd.so.%{amd_version_major} -o \
        libamd.so.%{amd_version} ../AMD/Lib/*.o -lm
    %__ln_s -f libamd.so.%{amd_version} libamd.so.%{amd_version_major}
    %__ln_s -f libamd.so.%{amd_version} libamd.so
    cp -p ../AMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License Doc/ChangeLog Doc/*.pdf ../Doc/AMD
popd

pushd BTF
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libbtf.so.%{btf_version_major} -o \
        libbtf.so.%{btf_version} ../BTF/Lib/*.o
    %__ln_s -f libbtf.so.%{btf_version} libbtf.so.%{btf_version_major}
    %__ln_s -f libbtf.so.%{btf_version} libbtf.so
    cp -p ../BTF/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/BTF
popd

pushd CAMD
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libcamd.so.%{camd_version_major} -o \
        libcamd.so.%{camd_version} ../CAMD/Lib/*.o -lm
    %__ln_s -f libcamd.so.%{camd_version} libcamd.so.%{camd_version_major}
    %__ln_s -f libcamd.so.%{camd_version} libcamd.so
    cp -p ../CAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License Doc/*.pdf ../Doc/CAMD
popd

pushd CCOLAMD
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libccolamd.so.%{ccolamd_version_major} -o \
        libccolamd.so.%{ccolamd_version} ../CCOLAMD/Lib/*.o -lm
    %__ln_s -f libccolamd.so.%{ccolamd_version} libccolamd.so.%{ccolamd_version_major}
    %__ln_s -f libccolamd.so.%{ccolamd_version} libccolamd.so
    cp -p ../CCOLAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/CCOLAMD
popd

pushd COLAMD
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libcolamd.so.%{colamd_version_major} -o \
        libcolamd.so.%{colamd_version} ../COLAMD/Lib/*.o -lm
    %__ln_s -f libcolamd.so.%{colamd_version} libcolamd.so.%{colamd_version_major}
    %__ln_s -f libcolamd.so.%{colamd_version} libcolamd.so
    cp -p ../COLAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/COLAMD
popd

%if "%{?enable_metis}" == "1"
CHOLMOD_FLAGS="%{optflags} -I%{_includedir}/metis -fPIC"
%else
CHOLMOD_FLAGS="%{optflags} -DNPARTITION -fPIC"
%endif
pushd CHOLMOD
  pushd Lib
    %make_build CFLAGS="$CHOLMOD_FLAGS"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libcholmod.so.%{cholmod_version_major} -o \
        libcholmod.so.%{cholmod_version} ../CHOLMOD/Lib/*.o \
        -L%{_libdir}/atlas %{atlaslibs} \
        libamd.so.%{amd_version_major} \
        libcamd.so.%{camd_version_major} libcolamd.so.%{colamd_version_major} \
        libccolamd.so.%{ccolamd_version_major} \
        libsuitesparseconfig.so.%{suitesparseconfig_version_major} -lm
    %__ln_s -f libcholmod.so.%{cholmod_version} libcholmod.so.%{cholmod_version_major}
    %__ln_s -f libcholmod.so.%{cholmod_version} libcholmod.so
    cp -p ../CHOLMOD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/*.pdf ../Doc/CHOLMOD
  cp -p Cholesky/License.txt ../Doc/CHOLMOD/Cholesky_License.txt
  cp -p Core/License.txt ../Doc/CHOLMOD/Core_License.txt
  cp -p MatrixOps/License.txt ../Doc/CHOLMOD/MatrixOps_License.txt
  cp -p Partition/License.txt ../Doc/CHOLMOD/Partition_License.txt
  cp -p Supernodal/License.txt ../Doc/CHOLMOD/Supernodal_License.txt
popd

#%%if 0%{?enable_csparse:0}
#pushd CSparse
#  pushd Source
#    %make_build CFLAGS="%{optflags} -fPIC"
#    cp -p cs.h ../../Include
#  popd
#  pushd ../Lib
#    %{__cc} -shared %{build_ldflags} -Wl,-soname,libcsparse.so.%{csparse_version_major} -o \
#        libcsparse.so.%{csparse_version} ../CSparse/Source/*.o -lm
#    %__ln_s libcsparse.so.%{csparse_version} libcsparse.so.%{csparse_version_major}
#    %__ln_s libcsparse.so.%{csparse_version} libcsparse.so
#    cp -p ../CSparse/Source/*.a ./
#  popd
#  mkdir ../Doc/CSparse/
#  cp -p Doc/* ../Doc/CSparse
#popd
#%%endif

pushd CXSparse
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libcxsparse.so.%{cxsparse_version_major} -o \
        libcxsparse.so.%{cxsparse_version} ../CXSparse/Lib/*.o -lm
    %__ln_s -f libcxsparse.so.%{cxsparse_version} libcxsparse.so.%{cxsparse_version_major}
    %__ln_s -f libcxsparse.so.%{cxsparse_version} libcxsparse.so
    cp -p ../CXSparse/Lib/*.a ./
  popd
  cp -p Include/cs.h ../Include
  mkdir ../Doc/CXSparse/
  cp -p Doc/* ../Doc/CXSparse
popd

pushd KLU
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libklu.so.%{klu_version_major} -o \
        libklu.so.%{klu_version} ../KLU/Lib/*.o \
        libamd.so.%{amd_version_major} libcolamd.so.%{colamd_version_major} \
        libbtf.so.%{btf_version_major} libcholmod.so.%{cholmod_version_major} \
        libsuitesparseconfig.so.%{suitesparseconfig_version_major}
    %__ln_s -f libklu.so.%{klu_version} libklu.so.%{klu_version_major}
    %__ln_s -f libklu.so.%{klu_version} libklu.so
    cp -p ../KLU/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/lesser.txt ../Doc/KLU
popd

pushd LDL
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libldl.so.%{ldl_version_major} -o \
        libldl.so.%{ldl_version} ../LDL/Lib/*.o
    %__ln_s -f libldl.so.%{ldl_version} libldl.so.%{ldl_version_major}
    %__ln_s -f libldl.so.%{ldl_version} libldl.so
    cp -p ../LDL/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/lesser.txt Doc/*.pdf ../Doc/LDL
popd

pushd UMFPACK
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,libumfpack.so.%{umfpack_version_major} -o \
        libumfpack.so.%{umfpack_version} ../UMFPACK/Lib/*.o \
        -L%{_libdir}/atlas %{atlaslibs} \
        libamd.so.%{amd_version_major} \
        libcholmod.so.%{cholmod_version_major} \
        libsuitesparseconfig.so.%{suitesparseconfig_version_major} -lm
    %__ln_s -f libumfpack.so.%{umfpack_version} libumfpack.so.%{umfpack_version_major}
    %__ln_s -f libumfpack.so.%{umfpack_version} libumfpack.so
    cp -p ../UMFPACK/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License Doc/ChangeLog Doc/gpl.txt Doc/*.pdf ../Doc/UMFPACK
popd

pushd SPQR
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cxx} -shared %{build_ldflags} -Wl,-soname,libspqr.so.%{spqr_version_major} -o \
        libspqr.so.%{spqr_version} ../SPQR/Lib/*.o \
        -L%{_libdir}/atlas -L%{_libdir} %{atlaslibs} \
        -ltbb -ltbbmalloc \
        libcholmod.so.%{cholmod_version_major} \
        libsuitesparseconfig.so.%{suitesparseconfig_version_major} -lm
    %__ln_s -f libspqr.so.%{spqr_version} libspqr.so.%{spqr_version_major}
    %__ln_s -f libspqr.so.%{spqr_version} libspqr.so
    cp -p ../SPQR/Lib/*.a ./
  popd
  cp -p Include/*.h* ../Include
  cp -p README{,_SPQR}.txt
  cp -p README_SPQR.txt Doc/* ../Doc/SPQR
popd

pushd RBio
  pushd Lib
    %make_build CFLAGS="%{optflags} -fPIC"
  popd
  pushd ../Lib
    %{__cc} -shared %{build_ldflags} -Wl,-soname,librbio.so.%{rbio_version_major} -o \
        librbio.so.%{rbio_version} ../RBio/Lib/*.o \
        libsuitesparseconfig.so.%{suitesparseconfig_version_major}
    %__ln_s -f librbio.so.%{rbio_version} librbio.so.%{rbio_version_major}
    %__ln_s -f librbio.so.%{rbio_version} librbio.so
    cp -p ../RBio/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License.txt ../Doc/RBio
popd

%install
install -d -m 755 %{buildroot}%{_libdir}
install -d -m 755 %{buildroot}%{_includedir}/%{name}

cp -pd Lib/*.so* %{buildroot}%{_libdir}/
cp -pd Include/*.h* %{buildroot}%{_includedir}/suitesparse/


%files
%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so

%files doc
%doc 

%files -n %{suitesparseconfig_packagename}
%{_libdir}/libsuitesparseconfig.so.%{suitesparseconfig_version_major}*

%files -n %{amd_packagename}
%{_libdir}/libamd.so.%{camd_version_major}*

%files -n %{btf_packagename}
%{_libdir}/libbtf.so.%{btf_version_major}*

%files -n %{camd_packagename}
%{_libdir}/libcamd.so.%{camd_version_major}*

%files -n %{ccolamd_packagename}
%{_libdir}/libccolamd.so.%{ccolamd_version_major}*

%files -n %{cholmod_packagename}
%{_libdir}/libcholmod.so.%{cholmod_version_major}*

%files -n %{colamd_packagename}
%{_libdir}/libcolamd.so.%{colamd_version_major}*

#%%if 0%{?enable_csparse:0}
#%%files -n %{csparse_packagename}
#%%defattr(-,root,root)
#%%{_libdir}/libcsparse.so.%{csparse_version_major}
#%%endif

%files -n %{cxsparse_packagename}
%{_libdir}/libcxsparse.so.%{cxsparse_version_major}*

%files -n %{klu_packagename}
%{_libdir}/libklu.so.%{klu_version_major}*

%files -n %{ldl_packagename}
%{_libdir}/libldl.so.%{ldl_version_major}*

%files -n %{umfpack_packagename}
%{_libdir}/libumfpack.so.%{umfpack_version_major}*

%files -n %{spqr_packagename}
%{_libdir}/libspqr.so.%{spqr_version_major}*

%files -n %{rbio_packagename}
%{_libdir}/librbio.so.%{rbio_version_major}*
